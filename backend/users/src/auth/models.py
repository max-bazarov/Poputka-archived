from datetime import datetime

from database import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (JSON, TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        String, Table)

from src.database import metadata

role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column(
        'permissions',
        JSON,
    ),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'User'

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, nullable=False)
    registered_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    role_id: int = Column(Integer, ForeignKey(role.c.id))
    email: str = Column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: str = Column(
        String(length=1024), nullable=False
    )
    is_active: bool = Column(
        Boolean, default=True, nullable=False
    )
    is_superuser: bool = Column(
        Boolean, default=False, nullable=False
    )
    is_verified: bool = Column(
        Boolean, default=False, nullable=False
    )
