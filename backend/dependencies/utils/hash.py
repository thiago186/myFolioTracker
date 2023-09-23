import os

import bcrypt
import jwt
from dotenv import load_dotenv

from dependencies.models.users import UserToLogin

load_dotenv()

def encrypt_password(password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
