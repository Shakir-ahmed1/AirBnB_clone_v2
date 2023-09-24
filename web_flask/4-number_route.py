#!/usr/bin/python3
""" hello HBNB """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays hello HBNB! page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ displays the uri passed to the text argument """
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ displays the uri passed to the text argument with default value """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_only(n):
    return f"{n}"


app.run(host='0.0.0.0', port=5000)
