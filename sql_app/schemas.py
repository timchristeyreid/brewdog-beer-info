from pydantic import BaseModel

# Create a BeerBase Pydantic schema to have common attributes whilst creating or reading data
class BeerBase(BaseModel):
    name: str
    tagline: str
    abv: int


class BeerCreate(BeerBase):
    pass


class Beer(BeerBase):
    id: int

    class Config:
        orm_mode = True