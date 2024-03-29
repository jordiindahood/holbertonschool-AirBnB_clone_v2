#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.city import City
import models


class State(BaseModel):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """returns the list of City instances"""
        instance_list = []
        for ins in models.storage.all(City).values():
            if ins.state_id == self.id:
                instance_list.append(ins)
