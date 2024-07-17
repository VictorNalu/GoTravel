#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    activities = relationship("Activity", back_populates="city")
    cultural_events = relationship("CulturalEvent",
                                   back_populates="city")
    destinations = relationship("Destination", back_populates="city")
    state = relationship("State", back_populates="cities")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
