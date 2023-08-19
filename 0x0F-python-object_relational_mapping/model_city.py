#!/usr/bin/python3

"""
Module that connects a python script to the database
"""

from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Defining the City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
