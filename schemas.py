from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, PositiveInt, Field, validator
from enum import Enum


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class AudioFileType(str, Enum):
    song = "song"
    podcast = "podcast"
    audiobook = "audiobook"


class AudioFileBase(BaseModel):
    name: str = Field(None)
    duration: PositiveInt = Field(default=1)
    uploaded_time: datetime = Field(default_factory=datetime.now)


class SongCreate(AudioFileBase):
    pass


class Song(AudioFileBase):
    id: int

    class Config:
        orm_mode = True


class PodcastCreate(AudioFileBase):
    host: str = Field(None)
    participants: List[str] = Field(None, max_items=10)


class Podcast(AudioFileBase):
    id: int

    class Config:
        orm_mode = True


class AudiobookCreate(AudioFileBase):
    author: str = Field(None)
    narrator: str = Field(None)


class Audiobook(AudioFileBase):
    id: int

    class Config:
        orm_mode = True