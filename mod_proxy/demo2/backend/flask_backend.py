import logging

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def secret():
    logging.info("hit secret.")
    return "<html>ssrf test</html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)