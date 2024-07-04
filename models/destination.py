#!/usr/bin/python3
"""Defines a module that contain class for destination"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Destination(BaseModel, Base):
    """Representation of a destination"""
    if models.storage_t == 'db':
        __tablename__ = 'destinations'
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        itineraries = relationship("Itinerary", secondary="itinerary_destinations",
                                   back_populates="destinations")
    else:
        name = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes destination"""
        super().__init__(*args, **kwargs)
