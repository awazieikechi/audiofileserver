from fastapi import FastAPI, Body, HTTPException, APIRouter
from fastapi_sqlalchemy import db
from models import Song, Podcast, Audiobook
import schemas
from typing import List, Dict, Optional


router = APIRouter()


@router.get("/audio/{audiofile_type}")
async def read_audiofiles(
    audiofile_type: schemas.AudioFileType, skip: int = 0, limit: int = 100
):
    if audiofile_type not in schemas.AudioFileType:
        raise HTTPException(status_code=400, detail="The request is invalid")

    if schemas.AudioFileType.song == audiofile_type:

        audiofile = db.session.query(Song).offset(skip).limit(limit).all()

    if schemas.AudioFileType.podcast == audiofile_type:

        audiofile = db.session.query(Podcast).offset(skip).limit(limit).all()

    if schemas.AudioFileType.audiobook == audiofile_type:

        audiofile = db.session.query(Audiobook).offset(skip).limit(limit).all()

    return audiofile


@router.get("/audio/{audiofile_type}/{audiofile_id}")
def read_audiofile(audiofile_type: schemas.AudioFileType, audiofile_id: int):

    if audiofile_type not in schemas.AudioFileType:
        raise HTTPException(status_code=400, detail="The request is invalid")

    if schemas.AudioFileType.song == audiofile_type:

        audiofile = db.session.query(Song).filter(Song.id == audiofile_id).first()

    if schemas.AudioFileType.podcast == audiofile_type:

        audiofile = db.session.query(Podcast).filter(Podcast.id == audiofile_id).first()

    if schemas.AudioFileType.audiobook == audiofile_type:

        audiofile = (
            db.session.query(Audiobook).filter(Audiobook.id == audiofile_id).first()
        )

    if audiofile is None:
        raise HTTPException(status_code=404, detail="File Not Found")
    return audiofile


@router.put("/audio/{audiofile_type}")
def create_audiofile(
    audiofile_type: schemas.AudioFileType,
    song: Optional[schemas.SongCreate] = None,
    podcast: Optional[schemas.PodcastCreate] = None,
    audiobook: Optional[schemas.AudiobookCreate] = None,
):
    if audiofile_type not in schemas.AudioFileType:
        raise HTTPException(status_code=400, detail="The request is invalid")

    if schemas.AudioFileType.song == audiofile_type:
        song.dict()
        db_audiofile = Song(
            name=song.name,
            duration=song.duration,
            uploaded_time=song.uploaded_time,
        )

    if schemas.AudioFileType.podcast == audiofile_type:
        podcast.dict()
        db_audiofile = Podcast(
            name=podcast.name,
            duration=podcast.duration,
            uploaded_time=podcast.uploaded_time,
            host=podcast.host,
            participants=podcast.participants,
        )

    if schemas.AudioFileType.audiobook == audiofile_type:

        db_audiofile = Audiobook(
            name=audiobook.name,
            author=audiobook.author,
            narrator=audiobook.narrator,
            duration=audiobook.duration,
            uploaded_time=audiobook.uploaded_time,
        )

    db.session.add(db_audiofile)
    db.session.commit()
    db.session.refresh(db_audiofile)
    raise HTTPException(status_code=200, detail="Action is Successful")
    return db_audiofile


@router.delete("/audio/{audiofile_type}/{audiofile_id}")
def delete_audiofile(audiofile_type: schemas.AudioFileType, audiofile_id: int):

    if audiofile_type not in schemas.AudioFileType:
        raise HTTPException(status_code=400, detail="The request is invalid")

    if schemas.AudioFileType.song == audiofile_type:

        audiofile = db.session.query(Song).filter(Song.id == audiofile_id).first()
        db.session.query(Song).filter(Song.id == audiofile_id).delete()

    if schemas.AudioFileType.podcast == audiofile_type:

        audiofile = db.session.query(Podcast).filter(Podcast.id == audiofile_id).first()
        db.session.query(Podcast).filter(Podcast.id == audiofile_id).delete()

    if schemas.AudioFileType.audiobook == audiofile_type:

        audiofile = (
            db.session.query(Audiobook).filter(Audiobook.id == audiofile_id).first()
        )
        db.session.query(Audiobook).filter(Audiobook.id == audiofile_id).delete()

    if audiofile is None:
        raise HTTPException(status_code=404, detail="File Not Found")

    raise HTTPException(status_code=200, detail="Action is Successful")


@router.patch("/audio/{audiofile_type}/{audiofile_id}")
def update_audiofile(
    audiofile_type: schemas.AudioFileType,
    audiofile_id: int,
    song: Optional[schemas.SongCreate] = None,
    podcast: Optional[schemas.PodcastCreate] = None,
    audiobook: Optional[schemas.AudiobookCreate] = None,
):

    if audiofile_type not in schemas.AudioFileType:
        raise HTTPException(status_code=400, detail="The request is invalid")

    if schemas.AudioFileType.song == audiofile_type:
        song.dict(exclude_unset=True)
        db_audiofile = db.session.query(Song).filter(Song.id == audiofile_id).first()
        for var, value in vars(song).items():
            setattr(db_audiofile, var, value) if value else None

    if schemas.AudioFileType.podcast == audiofile_type:
        podcast.dict(exclude_unset=True)
        db_audiofile = (
            db.session.query(Podcast).filter(Podcast.id == audiofile_id).first()
        )
        for var, value in vars(podcast).items():
            setattr(db_audiofile, var, value) if value else None

    if schemas.AudioFileType.audiobook == audiofile_type:
        audiobook.dict(exclude_unset=True)
        db_audiofile = (
            db.session.query(Audiobook).filter(Audiobook.id == audiofile_id).first()
        )
        for var, value in vars(audiobook).items():
            setattr(db_audiofile, var, value) if value else None

    if db_audiofile is None:
        raise HTTPException(status_code=404, detail="File Not Found")
    db.session.add(db_audiofile)
    db.session.commit()
    db.session.refresh(db_audiofile)
    raise HTTPException(status_code=200, detail="Action is Successful")
    return db_audiofile
