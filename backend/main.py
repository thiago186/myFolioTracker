import os
import jwt

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

# TODO: Define or import 'User' and 'users' before using them
# For example:
# class User(BaseModel):
#     username: str
#     ...
# users = []


@app.post("/register_user/")
async def register_user(user: User):
    for u in users:
        if u.username == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
    users.append(user)
    return {"message": "User created successfully"}
