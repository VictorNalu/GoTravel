#!/usr/bin/python3
""" Defines a User class model"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Destination(BaseModel, Base):
    """
    Destination Model

    Represents a destination within a trip.
    Stores information about places the user plans to visit.
    """
    __tablename__ = 'destinations'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    trip_id = Column(String(60), ForeignKey('trips.id'), nullable=False)
    description = Column(String(1024))
    address = Column(String(256))
    name = Column(String(128), nullable=False)
    city = relationship("City", back_populates="destinations")
    trip = relationship("Trip", back_populates="destinations")
