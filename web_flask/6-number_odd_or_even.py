#!/usr/bin/python3
"""start a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template

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
    """return a message"""
    text = escape(text)
    new_txt = text.replace("_", " ")
    return f"C {new_txt}"


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """return a message"""
    text = escape(text)
    new_txt = text.replace("_", " ")
    return f"Python {new_txt}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return a number given"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_num(n):
    """
    show a html template
    """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    show a html template
    """
    if n % 2 == 0:
        return render_template("5-number.html", n=f"{n} is even")
    else:
        return render_template("5-number.html", n=f"{n} is odd")

if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
