#!/usr/bin/python3
""" Defines a User class model"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Table, DateTime, ForeignKey
from sqlalchemy.orm import relationship


itinerary_activity = Table(
        'itinerary_activity', Base.metadata,
        Column('itinerary_id', String(60), ForeignKey('itineraries.id'),
               primary_key=True),
        Column('activity_id', String(60), ForeignKey('activities.id'),
               primary_key=True)
)


class Itinerary(BaseModel, Base):
    """
    Itinerary Model

    Represents a daily itinerary for a trip.
    Links to activities planned for each day.
    """
    __tablename__ = 'itineraries'
    trip_id = Column(String(60), ForeignKey('trips.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    trip = relationship("Trip", back_populates="itineraries")
    activities = relationship("Activity", secondary=itinerary_activity,
                              back_populates="itinerary")
