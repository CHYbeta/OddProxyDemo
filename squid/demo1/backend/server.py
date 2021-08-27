from flask import Flask, Response

app = Flask(__name__)


@app.route('/secret', methods=['GET'])
def secret():
    return "<html>secret</html>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
