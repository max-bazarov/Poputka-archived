from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Boolean,
    Integer,
    MetaData,
    String,
    TIMESTAMP,
    ForeignKey,
    Table,
    Column,
    JSON,
)

from database import Base

# from src.database import metadata
metadata = MetaData()

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

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey(role.c.id)),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
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
