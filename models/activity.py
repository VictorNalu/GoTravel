#!/usr/bin/python3
"""
defines activity class
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Activity(BaseModel, Base):
    """
    Activity Model

    Represents a specific activity planned within an itinerary.
    Stores details about individual activities or events.
    """
    __tablename__ = 'activities'

    itinerary_id = Column(String(60), ForeignKey('itineraries.id'),
                          nullable=False)
    cultural_event_id = Column(String(60), ForeignKey('cultural_events.id'))
    name = Column(String(128), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    location = Column(String(128))
    city_id = Column(String(60), ForeignKey('cities.id'))
    city = relationship("City", back_populates="activities")
    cultural_event = relationship("CulturalEvent", back_populates="activities")
    itinerary = relationship("Itinerary", back_populates="activities")
