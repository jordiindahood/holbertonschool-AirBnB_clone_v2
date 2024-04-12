#!/usr/bin/python3
"""start a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return a message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    return f"C {escape(text)}"


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
