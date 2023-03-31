from fastapi import FastAPI
from auth.auth_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead


app = FastAPI()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
