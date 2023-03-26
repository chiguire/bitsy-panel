import argparse
from flask import Flask, render_template
from flask_socketio import SocketIO
import logging

from bitsy_ledpanel.constants import (
    APP_NAME, 
    LOG_LEVEL,
    LOG_FORMAT,
)

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(name=APP_NAME)


class BitsyPanel:

    def __init__(self, port):
        self.port = port
        self.socket_async_mode = None
        self.app = Flask(import_name=APP_NAME)
        self.socket_ = SocketIO(self.app, async_mode=self.socket_async_mode)
        self.app.add_url_rule(rule='/', endpoint='index', view_func=self.index)

    def index(self):
        return render_template('index.html', sync_mode=self.socket_async_mode)

    def run(self):
        self.socket_.run(self.app, debug=True)
        
def main():
    parser = argparse.ArgumentParser(
        prog="bitsy_panel",
        description="Displays Bitsy games in a huge LED panel"
    )
    parser.add_argument("--port", required=True, help="Port number for webserver, this server only accepts connections from localhost")

    args = parser.parse_args()

    bitsy_panel = BitsyPanel(port = args.port)
    bitsy_panel.run()

if __name__ == "__main__":
    main()