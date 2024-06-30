#!/usr/bin/python3
"""Defines a module which contain a class for accommodation"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Table, Column, String, DateTime, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    accommodation_amenity = Table('accommodation_amenity', Base.metadata,
                                  Column('accommodation_id', String(60),
                                         ForeignKey('accommodations.id', onupdate='CASCADE',
                                                    ondelete='CASCADE'), primary_key=True),
                                  Column('amenity_id', String(60),
                                         ForeignKey('amenities.id', onupdate='CASCADE',
                                                    ondelete='CASCADE'), primary_key=True))

class Accommodation(BaseModel, Base):
    """Representation of an accommodation"""
    if models.storage_t == 'db':
        __tablename__ = 'accommodations'
        accommodation_id = Column(String(60), primary_key=True, nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        name = Column(String(128), nullable=False)
        address = Column(String(256), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        check_in = Column(DateTime, nullable=True)
        check_out = Column(DateTime, nullable=True)
        price = Column(Float, nullable=True)
        amenities = relationship("Amenity", secondary=accommodation_amenity,
                                 back_populates="accommodations")
        itinerary_id = Column(String(60), ForeignKey('itineraries.id'), nullable=False)
        itinerary = relationship("Itinerary", back_populates="accommodations")
        user = relationship("User", back_populates="accommodations")
        city = relationship("City", back_populates="accommodations")
    else:
        accommodation_id = ""
        user_id = ""
        city_id = ""
        name = ""
        address = ""
        number_rooms = 0
        max_guest = 0
        check_in = None
        check_out = None
        price = 0.0
        amenities = []
        itinerary_id = ""

    def __init__(self, *args, **kwargs):
        """initializes accommodation"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        from models.review import Review
        review_list = []
        all_reviews = models.storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """getter attribute returns the list of Amenity instances"""
        from models.amenity import Amenity
        amenity_list = []
        all_amenities = models.storage.all(Amenity)
        for amenity in all_amenities.values():
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list
