from flask import Flask

app = Flask(__name__)


@app.route('/public', methods=['GET'])
def public():
    return "public endpoint"


@app.route('/private', methods=['GET'])
def private():
    return "private endpoint"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
