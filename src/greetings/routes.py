from flask import jsonify

from greetings import app


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify(message="Hello World")
