import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

# class to store user info
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)

# class for Books Database
class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True)
    bookName = Column(String(250), nullable = False)
    authorName = Column(String(250), nullable = False)
    coverUrl = Column(String(450), nullable = False)
    description = Column(String(), nullable = False)
    category = Column(String(100), nullable = False)


engine = create_engine('sqlite:///BookCatalog.db')
Base.metadata.create_all(engine)
