from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

# Importing the Base class defined in database.py as each of the database models inherits from this.
from .database import Base

# Creating a class Beer that inherits from Base
class Beer(Base):
    __tablename__ = "beer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    tagline = Column(String)
    abv = Column(Integer)