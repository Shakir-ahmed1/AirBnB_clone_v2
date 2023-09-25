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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ lists all states in the storage """
    states = storage.all(State)
    for st in states:
        print(f'{states[st].id}: <B>{states[st].name}')
        for ct in states[st].cities:
            print(f"    {ct.name}")
        #    print(f'{st.cities[ct].id} <B>{{st.cities[ct].name}}')

    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run()
