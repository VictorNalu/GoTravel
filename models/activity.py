#!/usr/bin/python3
"""defines model activity class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship

class Activity(BaseModel, Base):
    """Representation of an activity"""
    if models.storage_t == 'db':
        __tablename__ = 'activities'
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        start_time = Column(DateTime, nullable=True)
        end_time = Column(DateTime, nullable=True)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        itinerary_id = Column(String(60), ForeignKey('itineraries.id'), nullable=False)
        itinerary = relationship("Itinerary", back_populates="activities")
        city = relationship("City", back_populates="activities")
        __table_args__ = (
            CheckConstraint('end_time >= start_time', name='check_end_time_after_start_time'),
        )

    else:
        name = ""
        description = ""
        start_time = None
        end_time = None
        location = ""
        itinerary_id = ""
