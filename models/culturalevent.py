#!/usr/bin/pythpn3
"""Defines a class for cultural event"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class CulturalEvent(BaseModel, Base):
    """
    Reps cultural events or festivals that can be incorporated into trips.
    This model allows the application to showcase local cultural experiences,
    particularly focusing on Nigerian festivals and traditions.
    """
    __tablename__ = 'cultural_events'
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    city = relationship("City", back_populates="cultural_events")
    activities = relationship("Activity", back_populates="cultural_event")
