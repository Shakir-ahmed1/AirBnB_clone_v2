#!/usr/bin/python3
""" hello HBNB """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ remove the current sqlalchemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def cities_by_states():
    """ lists all states in the storage """
    newst = []
    newam = []
    amenities = storage.all(Amenity)
    states = storage.all(State)
    for am in amenities:
        newam.append(amenities[am])
    for st in states:
        newst.append(states[st])
    return render_template('10-hbnb_filters.html', states=newst, amenities=newam)


if __name__ == '__main__':
    app.run()
