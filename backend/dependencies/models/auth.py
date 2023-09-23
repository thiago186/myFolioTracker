import os

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class JWToken(BaseModel):
    access_token: str
    token_type: str
