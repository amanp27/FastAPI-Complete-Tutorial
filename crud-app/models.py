"""
Using python we gonna define the table structure of the DB. Python classes will represent the tables in the database, and the attributes of those classes will represent the columns in the tables. This is done using SQLAlchemy's ORM (Object-Relational Mapping) capabilities.
"""

# Defining the table of the database using Python
from sqlalchemy import Column, Integer, String
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    enail = Column(String, unique=True, index=True)