import os
import time

import jwt
from dotenv import load_dotenv

from dependencies.models.users import UserToLogin
from dependencies.services.connectors.postgres_sql import get_user_by_email
from dependencies.utils.hash import verify_password

load_dotenv()

async def authenticate_user(user: UserToLogin):
    """ 
    1. Check if the user exists in the database.
    2. Authenticate a user and return a JWT token if the user is valid.
    """
    db_user = get_user_by_email(user.email)
    if not db_user:
        return False

    if not verify_password(user.password, db_user.hashed_password):
        return False

    token = jwt.encode(
        payload={
            "exp": time.time() + float(os.environ['JWT_EXPIRATION_TIME']),
            },
        key=os.environ["JWT_SECRET_KEY"], 
        algorithm="HS256"
    )
    return {"token": token}


