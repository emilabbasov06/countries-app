from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session

from ..models import CountryModel
from ..database import get_db


router = APIRouter(
  prefix='/api/countries',
  tags=['Countries']
)

@router.get('/')
def get_countries(db: Session = Depends(get_db)):
  countries = db.query(CountryModel).all()
  if not countries:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There is no table names countries')
  
  return countries

@router.get('/{id}')
def get_country(id: int, db: Session = Depends(get_db)):
  country = db.query(CountryModel).filter(CountryModel.id == int(id)).first()
  return country