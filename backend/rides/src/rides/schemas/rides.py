from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CarCreate(BaseModel):
    make: str
    model: str
    year: Optional[int] = None
    license_plate_number: str


class CarRead(CarCreate):
    id: int


class RideCreate(BaseModel):
    driver: int
    car: CarRead
    places: int
    destination: str
    departure_point: str
    time: datetime


class RideRead(RideCreate):
    id: int
