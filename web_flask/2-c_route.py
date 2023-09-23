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


@app.route('/c/<text>')
def c_text(text):
    """ displays the uri passed to the text argument """
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run()
