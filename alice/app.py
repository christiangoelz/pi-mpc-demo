#!/usr/bin/env python3
import argparse
from flask import Flask, render_template
from flask_socketio import SocketIO
import pty
import os
import subprocess
import select
import termios
import struct
import fcntl
import logging
import sys
import signal

logging.getLogger("werkzeug").setLevel(logging.ERROR)

__version__ = "0.5.0.2"

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")
app.config["SECRET_KEY"] = "secret!"
app.config["fd"] = None
app.config["child_pid"] = None
socketio = SocketIO(app)

ALICE_SCRIPT = "./scripts/run_alice.sh"  # Only this script can be run

def set_winsize(fd, row, col, xpix=0, ypix=0):
    """ Set the terminal window size """
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)

def read_and_forward_pty_output():
    """ Read output from Alice process and forward to client """
    max_read_bytes = 1024 * 20
    while True:
        socketio.sleep(0.01)
        if app.config["fd"]:
            (data_ready, _, _) = select.select([app.config["fd"]], [], [], 0)
            if data_ready:
                output = os.read(app.config["fd"], max_read_bytes).decode(errors="ignore")
                socketio.emit("pty-output", {"output": output}, namespace="/pty")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("pty-input", namespace="/pty")
def pty_input(data):
    """ Sends user input to Alice process """
    if app.config["fd"]:
        logging.debug(f"Received input from browser: {data['input']}")
        os.write(app.config["fd"], data["input"].encode())

@socketio.on("resize", namespace="/pty")
def resize(data):
    """ Resize terminal """
    if app.config["fd"]:
        set_winsize(app.config["fd"], data["rows"], data["cols"])

@socketio.on("connect", namespace="/pty")
def connect():
    """ Handles new client connection """
    logging.info("New client connected")

    if app.config["child_pid"]:
        logging.info("Alice already running")
        return

    (child_pid, fd) = pty.fork()
    if child_pid == 0:
        # Child process executes Alice script
        subprocess.run([ALICE_SCRIPT])
    else:
        # Parent process stores child details
        app.config["fd"] = fd
        app.config["child_pid"] = child_pid
        set_winsize(fd, 50, 50)

        socketio.start_background_task(target=read_and_forward_pty_output)
        logging.info(f"Started Alice with PID {child_pid}")

@socketio.on("disconnect", namespace="/pty")
def disconnect():
    """ Handles user disconnection """
    logging.info("Client disconnected")

    if app.config["child_pid"]:
        logging.info("Stopping Alice process")
        os.kill(app.config["child_pid"], signal.SIGTERM)
        app.config["child_pid"] = None
        app.config["fd"] = None

@app.route("/alice-stopped", methods=["POST"])
def alice_stopped():
    """ Handles Alice shutdown notification """
    logging.info("Received shutdown signal from Alice.")

    # Emit force disconnect event
    socketio.emit("force-disconnect", {}, namespace="/pty")

    return "OK", 200


def main():
    parser = argparse.ArgumentParser(description="Web-based terminal for Alice AI")
    parser.add_argument("-p", "--port", default=5000, help="Server port", type=int)
    parser.add_argument("--host", default="0.0.0.0", help="Host (use 0.0.0.0 for external access)")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    logging.basicConfig(
        format="%(levelname)s: %(message)s",
        stream=sys.stdout,
        level=logging.DEBUG if args.debug else logging.INFO,
    )
    
    logging.info(f"Serving on http://{args.host}:{args.port}")
    socketio.run(app, debug=args.debug, port=args.port, host=args.host, allow_unsafe_werkzeug=True)

if __name__ == "__main__":
    main()
