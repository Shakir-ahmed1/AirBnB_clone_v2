#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',String(60), ForeignKey('places.id')),
                      Column('amenity_id',String(60), ForeignKey('amenities.id')))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            from models.engine.file_storage import FileStorage
            storage = FileStorage()
            storage.reload()
            for k, v in storage.all().items():
                result = []
                if k.startswith(f'Review') and k.place_id == self.id:
                    result.append(k)
            return result


