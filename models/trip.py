#!/usr/bin/python3
""" Defines a trip class model"""

import models
from models.base_model import BaseModel, Base
from models.user import user_trip
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

trip_destination = Table(
        'trip_destination', Base.metadata,
        Column('trip_id', String(60),
               ForeignKey('trips.id'), primary_key=True),
        Column('destination_id', String(60),
               ForeignKey('destinations.id'), primary_key=True)
        )


class Trip(BaseModel, Base):
    """
    Represents a travel trip planned by a user.
    Contains basic trip information and relationships
    to other trip-related entities.
    """

    __tablename__ = 'trips'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    reviews = relationship("Review", back_populates="trip")
    user = relationship("User", secondary=user_trip,
                        back_populates="trips")
    destinations = relationship("Destination", secondary=trip_destination,
                                back_populates="trip",
                                cascade="all, delete")
    itineraries = relationship("Itinerary", back_populates="trip")
    accommodations = relationship("Accommodation", back_populates="trip")
    transportations = relationship("Transportation", back_populates="trip")
    expenses = relationship("Expense", back_populates="trip")

    def __init__(self, *args, **kwargs):
        """Initializes trip"""
        super().__init__(*args, **kwargs)
