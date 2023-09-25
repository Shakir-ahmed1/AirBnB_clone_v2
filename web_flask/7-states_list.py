#!/usr/bin/python3
""" hello HBNB """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove the current sqlalchemy session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ lists all states in the storage """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run()
