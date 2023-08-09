from sqlalchemy.orm import Session
from . import models, schemas
import json

# utility function to Read a single beer by id
def get_beer(db: Session, beer_id: int):
    return db.query(models.Beer).filter(models.Beer.id == beer_id).first()

# utility function to Read a single beer by name
def get_beer_by_name(db: Session, name: str):
    return db.query(models.Beer).filter(models.Beer.name == name).first()

# utility function to Read multiple beers
def get_beers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Beer).offset(skip).limit(limit).all()

# utility function to create a Beer
def create_beer(db: Session, beer: schemas.BeerCreate):
    db_beer = models.Beer(name=beer.name, tagline=beer.tagline, abv=beer.abv)
    db.add(db_beer)
    db.commit()
    db.refresh(db_beer)
    return db_beer

## Finding a way to create a database of beers through the app - this may be what is causing it to have an issue?
## i.e. when starting with a blank db the create, retrieve methods all work fine...
# utility function to add beers from IPA API
with open('beers.json', 'r') as openfile:
    data = json.load(openfile)

def create_beer_from_IPA(db: Session, beer: schemas.BeerCreate):
    for beer in data:
        db_beer = models.Beer(name = beer['name'], tagline = beer['tagline'], abv = beer['abv'])
    db.add(db_beer)
    db.commit()
    db.refresh(db_beer)
    return db_beer