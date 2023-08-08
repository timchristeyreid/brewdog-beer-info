from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from . database import SessionLocal, engine

# create the database tables
models.Base.metadata.create_all(bind=engine)

# create FastAPI instance
app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

## when using the dependency in a path operation function, declare it with the type Session imported from SQLALchemy
## The editor will know the db parameter is of type Session - and thus the available methods (.add(), .query(), .commit(), etc)

# FastAPI standard path operations
@app.post("/beers/", response_model=schemas.Beer)
def create_beer(beer: schemas.BeerCreate, db: Session = Depends(get_db)):
    db_beer = crud.get_beer_by_name(db, name=beer.name)
    if db_beer:
        raise HTTPException(status_code=400, detail="Beer already exists")
    return crud.create_beer(db=db, beer=beer)

@app.get("/beers/", response_model=list[schemas.Beer])
def read_beers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    beers = crud.get_beers(db, skip=skip, limit=limit)
    return beers

@app.get("/beers/{beer_id}", response_model=schemas.Beer)
def read_beer(beer_id: int, db: Session = Depends(get_db)):
    db_beer = crud.get_beer(db, beer_id=beer_id)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return db_beer