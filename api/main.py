from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import country

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