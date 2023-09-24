#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from . import storage
            from models.city import City
            filtered = []
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    filtered.append(value)
            return filtered

