import os
# import jwt
import logging


from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from dependencies.utils.hash import encrypt_password, verify_password
import dependencies.models.users as models_users
from dependencies.business_logic.authentication import authenticate_user
from dependencies.services.connectors.postgres_sql import (
    register_user,
    get_user_by_email
)

load_dotenv()
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


app = FastAPI()

# TODO: Define or import 'User' and 'users' before using them
# For example:
# class User(BaseModel):
#     username: str
#     ...
# users = []
print("Staarting app...")



@app.post("/users/register_user/")
async def register_user_endpoint(user: models_users.UserToRegister):
    user_exists = await get_user_by_email(user.email)
    if user_exists:
        raise HTTPException(status_code=409, detail="Email already registered")
    else:
        user.hashed_password = encrypt_password(user.password)
        try: 
            await register_user(user)
            return {"status_code": 201, "detail": "User created"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/get_auth/")
async def authenticate_user(user: models_users.UserToLogin):
    authentication = await authenticate_user(user)
    if authentication:
        return authentication
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")