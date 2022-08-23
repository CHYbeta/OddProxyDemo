from flask import Flask
from flask import request
import json
import logging


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    headers = request.headers
    return "Request headers:\n" + str(headers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
