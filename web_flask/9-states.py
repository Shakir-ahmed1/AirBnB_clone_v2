#!/usr/bin/python3
""" hello HBNB """
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove the current sqlalchemy session """
    storage.close()


@app.route('/states', defaults={'id': '-1'}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """ lists all states in the storage """
    states = storage.all(State)
    if id == '-1':
        new = []
        for st in states:
            new.append(states[st])
        return render_template('9-states.html', states=new, id='-1')
    for st in states:
        if states[st].id == id:
            return render_template('9-states.html', states=states[st])
    return render_template('9-states.html', states={})


if __name__ == '__main__':
    app.run()
