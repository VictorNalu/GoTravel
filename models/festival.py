#!/usr/bin/python3
"""Defines the Festival class."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship

class Festival(BaseModel, Base):
    """Representation of a festival"""
    if models.storage_t == 'db':
        __tablename__ = 'festivals'
        festival_id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        start_date = Column(Date, nullable=False)
        end_date = Column(Date, nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        itinerary_id = Column(String(60), ForeignKey('itineraries.id'), nullable=True)
        
        city = relationship("City", back_populates="festivals")
        state = relationship("State", back_populates="festivals")
        itinerary = relationship("Itinerary", back_populates="festivals")
    else:
        festival_id = ""
        name = ""
        description = ""
        start_date = None
        end_date = None
        city_id = ""
        state_id = ""
        itinerary_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes festival"""
        super().__init__(*args, **kwargs)
