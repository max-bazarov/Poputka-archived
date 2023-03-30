from fastapi import Depends, FastAPI
from auth.auth_config import auth_backend, fastapi_users
from auth.schemas import UserCreate, UserRead
from auth.models import User
from auth.auth_config import current_user


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


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"
