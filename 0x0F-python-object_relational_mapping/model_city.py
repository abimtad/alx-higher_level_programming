#!/usr/bin/python3

"""
python file that contains the class definition of a
City and an instance Base = declarative_base().
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
    name = Column(String(128), nullable=False)
