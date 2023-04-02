from pydantic import BaseModel


class RideRead(BaseModel):
    driver: int
    car: 