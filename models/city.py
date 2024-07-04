#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


city_festival = Table('city_festival', Base.metadata,
        Column('city_id', String(60), ForeignKey('cities.id')),
        Column('festival_id', String(60), ForeignKey('festivals.id'))
        )


class City(BaseModel, Base):
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        activities = relationship("Activity", back_populates="city")
        festivals = relationship("Festival", secondary='city_festival',
                                  back_populates="cities")
        accommodations = relationship("Accommodation",
                              backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
