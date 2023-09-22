from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

@app.post("/register_user/")
async def register_user(user: User):
    for u in users:
        if u.username == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
    users.append(user)
    return {"message": "User created successfully"}

