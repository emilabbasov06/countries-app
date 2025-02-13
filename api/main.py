from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from .routers import country

from .models import CountryModel
from .database import get_db

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

app.include_router(country.router)

@app.get('/')
def index():
  return {'message': 'Welcome to our CountriesAPI!'}