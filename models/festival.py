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

    @classmethod
    def search(cls, **kwargs):
        """Search for festivals based on criteria"""
        query = models.storage.query(cls)
        for key, value in kwargs.items():
            if hasattr(cls, key):
                if key in ['name', 'description']:
                    query = query.filter(getattr(cls, key).ilike(f'%{value}%'))
                elif key in ['city_id', 'state_id', 'itinerary_id']:
                    query = query.filter(getattr(cls, key) == value)
                elif key in ['start_date', 'end_date']:
                    query = query.filter(getattr(cls, key) == value)
        return query.all()

    @classmethod
    def suggest_for_itinerary(cls, city_id, start_date, end_date):
        """Suggest festivals for an itinerary"""
        return models.storage.query(cls).filter(
            cls.city_id == city_id,
            cls.start_date >= start_date,
            cls.end_date <= end_date
        ).all()
