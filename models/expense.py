import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Expense(BaseModel, Base):
    """
    Expense Model

    Represents financial expenses associated with a trip.
    Tracks various costs incurred during travel.
    """
    __tablename__ = 'expenses'

    trip_id = Column(String(60), ForeignKey('trips.id'), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(64), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String(256))
    trip = relationship("Trip", back_populates="expenses")
