import os

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class JWToken(BaseModel):
    """JWT to be received for validation for endpoints"""
    token: str