from flask import Flask
import logging


app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

@app.route('/public', methods=['GET'])
def public():
    app.logger.debug('hit public')
    return "gunicorn public endpoint"


@app.route('/private', methods=['GET'])
def private():
    app.logger.debug('hit private')
    return "gunicorn private endpoint"
