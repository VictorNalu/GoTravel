#!/usr/bin/python
""" holds class Accommodation"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table, Time
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    accommodation_amenity = Table('accommodation_amenity', Base.metadata,
                          Column('accommodation_id', String(60),
                                 ForeignKey('accommodations.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Accommodation(BaseModel, Base):
    """Representation of Accommodation """
    if models.storage_t == 'db':
        __tablename__ = 'accommodations'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price = Column(Integer, nullable=False, default=0)
        check_in = Column(Time, nullable=True)
        check_out = Column(Time, nullable=True)
        itinerary_id = Column(String(60), ForeignKey('itineraries.id'), nullable=True)
        itinerary = relationship("Itinerary", back_populates="accommodations")
        reviews = relationship("Review",
                               backref="accommodation",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=accommodation_amenity,
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price = 0
        check_in = None
        check_out = None
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Accommodation"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
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
