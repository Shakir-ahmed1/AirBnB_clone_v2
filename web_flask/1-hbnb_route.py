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


if __name__ == '__main__':
    app.run()
