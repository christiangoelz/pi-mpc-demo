#!/bin/bash

# Define path variables for easy updates and management
MYSELF="Alice"
PROJECT_DIR="/home/christian/${MYSELF,,}"
WEB_SERVER_SCRIPT="$PROJECT_DIR/third_party/federatedsecure/webserver-connexion/src/__main__.py"
FDRSC_SCRIPT="$PROJECT_DIR/src/${MYSELF,,}.py"
XTERM_LOG_DIR="$PROJECT_DIR/src/"
CONFIG_FILE="$PROJECT_DIR/config/p2p.cfg"

# Extract IP and PORT for this instance from the config file
get_ip_and_port() {
    # Extract the addr line from the specified section and parse the IP and port
    addr=$(awk -F' *= *' -v myself="$MYSELF" '
        /^\[.*\]/{section=$0} 
        section=="[" myself "]" && $1=="addr" {print $2}
    ' "$CONFIG_FILE")

    # Extract IP and port using regular expression
    if [[ $addr =~ http://([0-9a-zA-Z\.\-]+):([0-9]+) ]]; then
        ip="${BASH_REMATCH[1]}"
        port="${BASH_REMATCH[2]}"
    else
        echo "Error: Invalid address format in $CONFIG_FILE"
        exit 1
    fi
}

# Function to extract server addresses from the config file
parse_servers() {
    awk -F' *= *' -v myself="$MYSELF" '
        /^\[.*\]/{section=$0} 
        section!~"\[" myself "\]" && section~/^\[[A-Za-z]+\]$/ {if ($1 == "addr") print $2}
    ' "$CONFIG_FILE"
}

# Function to check if a web server is reachable
is_reachable() {
    curl -s --head --request GET "$1" &>/dev/null
}

# Wait until all required web servers are reachable
wait_for_servers() {
    # Collect the server addresses
    declare -a servers
    while IFS= read -r addr; do
        servers+=("$addr")
    done < <(parse_servers)

    echo "Waiting for all parties to join..."

    # Loop through all servers and wait until they are reachable
    for server in "${servers[@]}"; do
        while ! is_reachable "$server"; do
            sleep 2
        done
    done
    echo "All parties now reachable!"
}

# Start the server
start_server() {
    python "$WEB_SERVER_SCRIPT" host=0.0.0.0 port=$port > /dev/null 2>&1 &
    sleep 5  # Give the server a little time to start up.
    
    timeout=5
    while ! nc -z $ip $port &>/dev/null && [ $timeout -gt 0 ]; do
        sleep 0.1
        ((timeout--))
    done

    if [ $timeout -le 0 ]; then
        echo "Server failed to start on port $port"
        exit 1
    fi
    sleep 0.5
}

# Stop the server
stop_servers() {
    fuser -k "$port/tcp" > /dev/null 2>&1 &
}

# Ensure the config file exists before continuing
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file $CONFIG_FILE not found."
    exit 1
fi

# Ensure that the server is not already running
get_ip_and_port
stop_servers
echo "" > "$XTERM_LOG_DIR/terminal_output.txt"  # Clear the terminal log before starting
python -c "from utils import *; disp_middle(text='Alice', fontsize=14)"
ssh -i ~/.ssh/id_rsa christian@Bob.local 'bash ~/start.sh' > /dev/null 2>&1 &
ssh -i ~/.ssh/id_rsa christian@Charlie.local 'bash ~/start.sh' > /dev/null 2>&1 &
start_server > /dev/null 2>&1 &
wait_for_servers
python "$FDRSC_SCRIPT"
sudo env "PYTHONPATH=$PYTHONPATH" /home/christian/alice/venv/bin/python -m /home/christian/alice/src/alice.py
stop_servers > /dev/null 2>&1 &
echo "You can close the window now!"
python -c "from utils import *; disp_middle(text='', fontsize=14)"
