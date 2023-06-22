#!/usr/bin/python3
""" database storage engine managing module """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

H_USER = getenv('HBNB_MYSQL_USER')
H_PWD = getenv('HBNB_MYSQL_PWD')
H_HOST = getenv('HBNB_MYSQL_HOST', 'localhost')
H_DB = getenv('HBNB_MYSQL_DB')
H_ENV = getenv('HBNB_ENV')


class DBStorage:
    """ database storage engine """
    __engine = None
    __session = None

    def __init__(self):
        """ initializes the class """
        self.__engine = create_engine(
            f'mysql+mysqldb://{H_USER}:{H_PWD}@{H_HOST}:3306/{H_DB}',
            pool_pre_ping=True)
        if H_ENV == 'test':
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """ filters objects by the given cls """
        result = {}
        if cls is not None:
            tb = [cls]
        else:
            tb = [State, City]
        
        for t in tb:
            # converts the tuple to dictionary
            for v in self.__session.query(t).all():
                print(type(v))
                temp = {c.name: getattr(v, c.name) for c in v.__table__.columns}
                result[t.__name__ + '.' + temp['id']] = v

        return result

    def new(self, obj):
        """ adds the object to the current database session"""
        self.__session.add(obj)

    def save(self, obj=None):
        """ commits all changes """
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
