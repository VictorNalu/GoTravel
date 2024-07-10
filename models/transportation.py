#!/usr/bin/python3
""" Defines a User class model"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Transportation(BaseModel, Base):
    """
    Transportation Model

    Represents travel arrangements within a trip.
    Stores details about various modes of transportation used.
    """
    __tablename__ = 'transportations'
    trip_id = Column(String(60), ForeignKey('trips.id'), nullable=False)
    type = Column(String(64), nullable=False)  # e.g., "flight", "train", "bus"
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    departure_location = Column(String(128), nullable=False)
    arrival_location = Column(String(128), nullable=False)
    trip = relationship("Trip", back_populates="transportations")
