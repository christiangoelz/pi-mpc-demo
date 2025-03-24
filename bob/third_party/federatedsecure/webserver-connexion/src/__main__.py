#!/usr/bin/env python3

"""
the main module
"""

import sys
import connexion

from flask import current_app

from federatedsecure.server.bus import Bus


def main(**kwargs):
    """runs the webserver"""

    # enable the following line to log endpoint traffic
    # logging.basicConfig(level=logging.INFO)

    bus = Bus()

    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('openapi.yaml',
                arguments={'title': 'Federated Secure Computing'},
                pythonic_params=True)

    with app.app.app_context():
        current_app.bus = bus

    @app.app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,PATCH,DELETE')
        return response

    app.run(import_string=None, **kwargs)


if __name__ == '__main__':

    main(**dict([kv[0], int(kv[1]) if str.isdigit(kv[1]) else kv[1]]
                for kv in [arg.split('=') for arg in sys.argv[1:]]))
