import os

import bcrypt
import jwt
from dotenv import load_dotenv

from dependencies.models.users import UserToLogin

load_dotenv()

def encrypt_field(field: str):
    hashed_field = bcrypt.hashpw(field.encode('utf-8'), bcrypt.gensalt())
    return hashed_field.decode('utf-8')

def verify_field(field: str, hashed_field: str):
    return bcrypt.checkpw(field.encode('utf-8'), hashed_field.encode('utf-8'))
