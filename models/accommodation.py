#!/usr/bin/python3
""" Defines a User class model"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Accommodation(BaseModel, Base):
    """
    Accommodation Model

    Represents lodging arrangements for a trip.
    Stores details about where the user plans to stay.
    """
    __tablename__ = 'accommodations'

    trip_id = Column(String(60), ForeignKey('trips.id'), nullable=False)
    name = Column(String(128), nullable=False)
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    address = Column(String(256))
    trip = relationship("Trip", back_populates="accommodations")
