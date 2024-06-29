#!/usr/bin/python3
"""holds class Itinerary"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Itinerary(BaseModel, Base):
    """Representation of an itinerary """
    if models.storage_t == 'db':
        __tablename__ = 'itineraries'
        itinerary_id = Column(String(60), primary_key=True, nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        start_date = Column(DateTime, nullable=False)
        end_date = Column(DateTime, nullable=False)
        user = relationship("User", back_populates="itineraries")
        accommodations = relationship("Accommodation", back_populates="itinerary")
        activities = relationship("Activity", back_populates="itinerary")
        destinations = relationship("Destination", secondary="itinerary_destinations", back_populates="itineraries")
    else:
        itinerary_id = ""
        user_id = ""
        start_date = None
        end_date = None
        accommodations = []
        activities = []
        destinations = []

    def __init__(self, *args, **kwargs):
        """initializes itinerary"""
        super().__init__(*args, **kwargs)

    def add_destination(self, destination):
        """Add a destination to the itinerary"""
        if models.storage_t != 'db':
            self.destinations.append(destination)

    def add_accommodation(self, accommodation):
        """Add an accommodation to the itinerary"""
        if models.storage_t != 'db':
            self.accommodations.append(accommodation)

    def add_activity(self, activity):
        """Add an activity to the itinerary"""
        if models.storage_t != 'db':
            self.activities.append(activity)
