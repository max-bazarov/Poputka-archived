from typing import Optional

from pydantic import BaseModel


class UserRead(BaseModel):
    username: str


class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
