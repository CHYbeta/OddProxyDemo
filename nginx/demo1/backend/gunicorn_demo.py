from flask import Flask

app = Flask(__name__)


@app.route('/public', methods=['GET'])
def public():
    return "gunicorn public endpoint"


@app.route('/private', methods=['GET'])
def private():
    return "gunicorn private endpoint"
