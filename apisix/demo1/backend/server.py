from flask import Flask, Response

app = Flask(__name__)


@app.route('/public', methods=['GET'])
def public():
    return "<html>public</html>"


@app.route('/private', methods=['GET'])
def secret():
    return "<html>private</html>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
