import os
import time

import jwt
from dotenv import load_dotenv

from dependencies.models.users import UserToLogin
from dependencies.models.auth import JWToken
from dependencies.services.connectors.postgres_sql import get_user_by_email
from dependencies.utils.hash import verify_field

load_dotenv()

async def authenticate_user(user: UserToLogin):
    """ 
    1. Check if the user exists in the database.
    2. Authenticate a user and return a JWT token if the user is valid.
    """
    db_user = await get_user_by_email(user.email)
    if not db_user:
        return False

    if not verify_field(user.password, db_user.hashed_password):
        return False

    token = jwt.encode(
        payload={
            "sub": str(db_user.id),
            "exp": time.time() + float(os.environ['JWT_EXPIRATION_TIME']),
            },
        key=os.environ["JWT_SECRET_KEY"], 
        algorithm=os.environ['JWT_ALGORITHM']
    )
    return token

async def authenticate_token(token: str):
    if token.startswith("Bearer "):
        token = token[7:]
    try:
        decoded_token = jwt.decode(
            token,
            key=os.environ["JWT_SECRET_KEY"],
            algorithms=[os.environ['JWT_ALGORITHM']]
        )
        return {"authenticated": True, "reason": "Valid Token", "userid": decoded_token["sub"]}

    except jwt.ExpiredSignatureError:
        return {"authenticated": False, "reason": "Token expired"}
    except jwt.InvalidTokenError:
        return {"authenticated": False, "reason": "Invalid token"}


    
