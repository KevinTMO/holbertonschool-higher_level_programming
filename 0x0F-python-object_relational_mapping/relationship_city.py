#!/usr/bin/python3
"""
Defining a class named City who inherits from Base
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Creating a table named states and adding two fields (id, name)
    and defining their attrs
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
