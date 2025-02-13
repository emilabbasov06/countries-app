from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class CountryModel(Base):
  __tablename__ = 'countries'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  country = Column(String(255))
  capital = Column(Text)
  population = Column(Integer)
  area = Column(Float)