from typing import Optional
from pydantic import BaseModel


class CarRead(BaseModel):
    id: int
    make: str
    model: str
    year: int
    license_plate_number: str


class CarCreate(BaseModel):
    make: str
    model: str
    year: Optional[int] = None
    license_plate_number: str


class RideRead(BaseModel):
    driver: int
    car: CarRead
