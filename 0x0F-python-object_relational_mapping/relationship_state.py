#!/usr/bin/python3
"""
Defining a class named State who inherits from Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Creating a table named states and adding two fields (id, name)
    and defining their attrs
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
