import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship


class Accommodation(BaseModel, Base):
    """Representation of an accommodation"""
    if models.storage_t == 'db':
        __tablename__ = 'accommodations'
        name = Column(String(128), nullable=False)
        address = Column(String(256), nullable=True)
        check_in = Column(DateTime, nullable=True)
        check_out = Column(DateTime, nullable=True)
        price = Column(Float, nullable=True)
        amenities = Column(String(512), nullable=True)
        itinerary_id = Column(String(60), ForeignKey('itineraries.id'), nullable=False)
        itinerary = relationship("Itinerary", back_populates="accommodations")
    else:
        name = ""
        address = ""
        check_in = None
        check_out = None
        price = 0.0
        amenities = ""
        itinerary_id = ""

    def __init__(self, *args, **kwargs):
        """initializes accommodation"""
        super().__init__(*args, **kwargs)
