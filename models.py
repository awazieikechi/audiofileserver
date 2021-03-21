from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.types import PickleType
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from sqlalchemy.ext.mutable import MutableComposite
from sqlalchemy.ext.mutable import MutableDict, MutableList, MutableSet


Base = declarative_base()
metadata = Base.metadata


class Song(Base):

    __tablename__ = "songs"

    id = Column(INTEGER, primary_key=True, unique=True, index=True)
    name = Column(String(100), nullable=False)
    duration = Column(INTEGER, nullable=False)
    uploaded_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Podcast(Base):

    __tablename__ = "podcasts"

    id = Column(INTEGER, primary_key=True, unique=True, index=True)
    name = Column(String(100), nullable=False)
    duration = Column(INTEGER, nullable=False)
    uploaded_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    host = Column(String(100), nullable=False)
    participants = Column(MutableList.as_mutable(PickleType), default=[])


class Audiobook(Base):

    __tablename__ = "audiobooks"

    id = Column(INTEGER, primary_key=True, unique=True, index=True)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    narrator = Column(String(100), nullable=False)
    duration = Column(INTEGER, nullable=False)
    uploaded_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
