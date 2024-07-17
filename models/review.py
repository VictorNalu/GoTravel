#!/usr/bin/python
""" holds class Review"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Representation of Review """
    __tablename__ = 'reviews'
    trip_id = Column(String(60), ForeignKey('trips.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    trip = relationship("Trip", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
