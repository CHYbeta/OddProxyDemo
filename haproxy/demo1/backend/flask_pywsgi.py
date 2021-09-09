import logging

from flask import Flask
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/secret', methods=['GET', 'POST'])
def secret():
    logging.info("hit secret.")
    return "<html>secret</html>"


@app.route('/public', methods=['GET', 'POST'])
def public():
    logging.info("hit public.")
    return "<html>public</html>"


if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 8000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
