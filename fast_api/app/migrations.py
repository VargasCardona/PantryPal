"""
This module defines the database migrations for the application.
Attributes:
  Base: The declarative base class for SQLAlchemy models.
  DATABASE_URL: The database connection URL constructed from the settings.
  engine: The SQLAlchemy engine instance for connecting to the database.
Usage:
  This module is used to define and manage the database schema for the application.
  It includes the User model and the necessary configuration to connect to the database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

Base = declarative_base()


class User(Base):
    """
    A class used to represent a user in the database.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    full_name = Column(String)
    profile_picture = Column(String)


# Database configuration
DATABASE_URL = (
    f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}:"
    + f"{DATABASE['port']}/{DATABASE['name']}"
)
engine = create_engine(DATABASE_URL)

# Create the database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
