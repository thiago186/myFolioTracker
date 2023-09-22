"""
    This file contains the classes that represent the tables in the database.
"""
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime


from sqlmodel import Field, SQLModel


class UUIDModel(SQLModel):
    """Base class for all models that use UUID as primary key"""
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False
        )


class TimestampModel(SQLModel):
    """Base class for all models that use timestamps"""
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )


class UserBase(SQLModel):
    """Base class for all user models"""
    username:str = Field(nullable=False)
    email:str = Field(nullable=False)
    hashed_password: str
    last_login: Optional[datetime] = None
    is_active: bool = True
    is_admin: bool = False
    role: str= 'common'


class Users(UserBase, UUIDModel, TimestampModel, table=True):
    """Class that represents the users table in the database"""
