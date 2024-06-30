#!/usr/bin/python3
"""holds class Itinerary"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Itinerary(BaseModel, Base):
    """Representation of an itinerary """
    if models.storage_t == 'db':
        __tablename__ = 'itineraries'
        itinerary_id = Column(String(60), primary_key=True, nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        start_date = Column(DateTime, nullable=False)
        end_date = Column(DateTime, nullable=False)
        user = relationship("User", back_populates="itineraries")
        accommodations = relationship("Accommodation", back_populates="itinerary")
        activities = relationship("Activity", back_populates="itinerary")
        destinations = relationship("Destination", secondary="itinerary_destinations", back_populates="itineraries")
        festivals = relationship("Festival", back_populates="itinerary")
    else:
        itinerary_id = ""
        user_id = ""
        start_date = None
        end_date = None
        accommodations = []
        activities = []
        destinations = []
        festivals = []

    def __init__(self, *args, **kwargs):
        """initializes itinerary"""
        super().__init__(*args, **kwargs)

    @property
    def destination(self):
        """getter attribute returns the list of destination instances"""
        from models.destination import Destination
        dest_list = []
        all_dest = models.storage_t.all(Destination)
        for dest in all_dest.values():
            if dest.itinerary_id == self.id:
                dest_list.append(dest)
        return dest_list

    @property
    def accommodation(self):
        """getter attr reurns list of all accomodation in Destination instances"""
        from models.accommodation import Accommodation

        accm_list = []
        all_accm = models.storage_t.all(Accommodation)
        for accm in all_accm.values():
            if accm.itinerary_id == self.id:
                acccm_list.append(accm)
        return accm_list

    @property
    def activity(self):
        """getter attr returns all activities in Activity instance"""
        from models.activity import Activity
        activity_list = []
        all_act = models.storage_t.all(Activity)
        for activ in all_act.values():
            if activ.itinerary_id == self.id:
                activity_list.append(activ)
        return activity_list

    @property
    def festival(self):
        """getter attr returns all festivals in Festival instance"""
        from models.festival import Festival
        festival_list = []
        all_fest = models.storage_t.all(Festival)
        for fest in all_fest.values():
            if fest.itinerary_id == self.id:
                festival_list.append(fest)
        return festival_list
