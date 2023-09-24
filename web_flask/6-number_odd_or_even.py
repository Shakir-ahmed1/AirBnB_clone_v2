#!/usr/bin/python3
""" hello HBNB """
from flask import Flask, render_template
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
    """ displays the given text in the number path if it is integer """
    return f"{n}"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ prints the given integer and displays it inside a template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ displays if the given integer is even or odd"""
    parity = 'odd'
    if n % 2 == 0:
        parity = 'even'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


app.run(host='0.0.0.0', port=5000)
