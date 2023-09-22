from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    '''User model to interact with the Database'''

    user_id: UUID
    username: str
    email: str
    hashed_password: str
    created_at: datetime
    last_login: datetime = None
    is_active: bool = True
    is_admin: bool = False
    role: str

    class Config:
        from_attributes = True
