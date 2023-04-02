from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    username: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
