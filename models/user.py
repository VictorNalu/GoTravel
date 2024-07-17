#!/usr/bin/python3
""" Defines a User class model"""

from models.base_model import BaseModel, Base
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5

user_trip = Table(
        'user_trip', Base.metadata,
        Column('user_id', String(60), ForeignKey('users.id'),
               primary_key=True),
        Column('trip_id', String(60), ForeignKey('trips.id'),
               primary_key=True)
)


class User(BaseModel, Base):
    """
    Represents a user of the travel planning application.
    Stores user authentication information and links to their trips.
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship("Review", back_populates="user")
    trips = relationship("Trip", secondary=user_trip,
                         back_populates="user",
                         cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
