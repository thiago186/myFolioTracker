from datetime import datetime

from uuid import uuid4
from uuid import UUID

from pydantic import BaseModel
from typing import Optional
from pydantic.fields import Field

class UserToLogin(BaseModel):
    """User received on the login endpoint"""
    email: str
    password: str

class UserToRegister(BaseModel):
    """
    User class to be received on the API endpoint.
    The password received is not hashed yet.
    """
    user_id: UUID = Field(
        default_factory=uuid4
    )
    username: str
    email: str
    password: str
    hashed_password: Optional[str] = None
    created_at: Optional[datetime] = Field(
        default_factory=datetime.now,
    )
    last_login: Optional[datetime]
    is_admin: bool = False
    is_active: Optional[bool] = True
    role : Optional[str] = "commonuser"

    
class UserModel(BaseModel):
    """
    User model to interact with the API
    """
    user_id: UUID=Field(
        default_factory= uuid4,
        )
    username: str
    email: str
    hashed_password: str
    created_at: datetime
    last_login: datetime
    is_active: bool
    is_admin: bool
    role: Optional[str] = "commonuser"

    class Config:
        from_attributes = True
