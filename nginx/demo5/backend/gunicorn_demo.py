from flask import Flask, request, make_response
import logging


app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

@app.route('/<path:path>')
def allroute(path):
    try:
        resp_header = request.args.get("resp_header", "")
        resp_header_value = request.args.get("resp_header_value", "")
        add_header_json = {}
        if resp_header and resp_header_value:
            add_header_json = {resp_header: resp_header_value}
        return 'Hello world', 200, add_header_json

    except Exception as e:
        print(e)
