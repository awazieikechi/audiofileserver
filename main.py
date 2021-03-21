from fastapi import Depends, FastAPI, Header, HTTPException

from routers import audio

import os, sys

from fastapi_sqlalchemy import DBSessionMiddleware

from dotenv import load_dotenv

# this line is to connect to our base dir and connect to our .env file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(audio.router)
