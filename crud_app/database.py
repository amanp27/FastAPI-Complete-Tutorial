""" 
Helps setup DB connection amd provide components for ORM
Centralized DB setup, making it resusable across the app

# create_engine():
- Establish the connetion with database

# connect_args():
- SQLite-specific to allow connection sharing across threads
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Establish the connection with SQL database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)
# ------------------------------------------------------------------------
# SessionMaker: 
# Helps to create new databases sessions 
# autoflush= False: SQLAlchemy will not automatically flush changes to the DB unless you explicitly commited or refreshed the session.
# autocommit= False: means disables automatic commit after each query, commit manually
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ------------------------------------------------------------------------
# Base: declarative base class for defining ORM models. It provides the foundation for creating database tables and mapping them to Python classes.
Base = declarative_base()
