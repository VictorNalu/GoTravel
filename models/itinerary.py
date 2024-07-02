#!/usr/bin/python3
"""holds class Itinerary"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Table, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime

itinerary_destination = Table('itinerary_destinations', Base.metadata,
                              Column('itinerary_id', String(60),
                                     ForeignKey('itineraries.id'), primary_key=True),
                              Column('destination_id', String(60),
                                     ForeignKey('destinations.id'), primary_key=True)
                              )

class Itinerary(BaseModel, Base):
    """Representation of an itinerary """
    if models.storage_t == 'db':
        __tablename__ = 'itineraries'
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        status = Column(String(20), default='planned')
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        start_date = Column(DateTime, nullable=False)
        end_date = Column(DateTime, nullable=False)
        user = relationship("User", back_populates="itineraries")
        accommodations = relationship("Accommodation", back_populates="itinerary")
        activities = relationship("Activity", back_populates="itinerary")
        destinations = relationship("Destination", secondary="itinerary_destinations", back_populates="itineraries")
        festivals = relationship("Festival", back_populates="itinerary")
        __table_args__ = (
            CheckConstraint('end_date >= start_date', name='check_end_date_after_start_date'),
        )
    else:
        name = ""
        description = ""
        user_id = ""
        status = ""
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
        if models.storage_t == 'db':
            return self.destinations
        else:
            dest_list = []
            all_dest = models.storage_t.all(Destination)
            for dest in all_dest.values():
                if dest.itinerary_id == self.id:
                    dest_list.append(dest)
            return dest_list

    @property
    def total_activities(self):
        """Return the total number of activities in the itinerary"""
        if models.storage_t == 'db':
            return len(self.activities)
        else:
            from models.activity import Activity
            return len([act for act in models.storage.all(Activity).values() if act.itinerary_id == self.id])

    @property
    def accommodation(self):
        """getter attribute returns list of all accommodation instances"""
        from models.accommodation import Accommodation
        if models.storage_t == 'db':
            return self.accommodations
        else:
            accm_list = []
            all_accm = models.storage_t.all(Accommodation)
            for accm in all_accm.values():
                if accm.itinerary_id == self.id:
                    accm_list.append(accm)
            return accm_list

    @property
    def activity(self):
        """getter attribute returns all activities in Activity instance"""
        from models.activity import Activity
        if models.storage_t == 'db':
            return self.activities
        else:
            activity_list = []
            all_act = models.storage_t.all(Activity)
            for activ in all_act.values():
                if activ.itinerary_id == self.id:
                    activity_list.append(activ)
            return activity_list

    @property
    def festival(self):
        """getter attribute returns all festivals in Festival instance"""
        from models.festival import Festival
        if models.storage_t == 'db':
            return self.festivals
        else:
            festival_list = []
            all_fest = models.storage_t.all(Festival)
            for fest in all_fest.values():
                if fest.itinerary_id == self.id:
                    festival_list.append(fest)
            return festival_list

    @property
    def duration(self):
        """Calculate the duration of the itinerary in days"""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        return None

    def remove_activity(self, activity_id):
        """Remove an activity from the itinerary"""
        if models.storage_t == 'db':
            self.activities = [act for act in self.activities if act.id != activity_id]
        else:
            from models.activity import Activity
            activity = models.storage.get(Activity, activity_id)
            if activity and activity.itinerary_id == self.id:
                activity.itinerary_id = None
        models.storage.save()

    def add_activity(self, activity):
        """Add an activity to the itinerary"""
        if models.storage_t == 'db':
            self.activities.append(activity)
        else:
            activity.itinerary_id = self.id
        models.storage.save()

    def is_current(self):
        """Check if the itinerary is currently ongoing"""
        now = datetime.now()
        return self.start_date <= now <= self.end_date
