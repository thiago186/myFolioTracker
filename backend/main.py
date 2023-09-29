import os
import logging


from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from dependencies.utils.hash import encrypt_field, verify_field
import dependencies.models.users as models_users
from dependencies.models.auth import JWToken
from dependencies.business_logic.authentication import authenticate_user
from dependencies.services.connectors.postgres_sql import (
    register_user,
    get_user_by_email
)

load_dotenv()
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8082",
    "*",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# TODO: Define or import 'User' and 'users' before using them
# For example:
# class User(BaseModel):
#     username: str
#     ...
# users = []
print("Staarting app...")



@app.post("/users/register_user/")
async def register_user_endpoint(user: models_users.UserToRegister):
    """
    Register the received user in the database if it doesn't exists yet.
    Receives a user object with the following fields:
     - email
     - 
    """

    user_exists = await get_user_by_email(user.email)
    # print(f"user_exists: {user_exists}")
    if user_exists:
        raise HTTPException(status_code=409, detail="Email already registered")
    else:
        user.hashed_password = encrypt_field(user.password)
        try: 
            await register_user(user)
            return {"status_code": 201, "detail": "User created"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@app.post("/users/login/")
async def authenticate_user_endpoint(user: models_users.UserToLogin):
    """
    Receives email and password and returns a jwt token if user is authenticated.
    """
    print(f"received user: {user}")
    authentication = await authenticate_user(user)
    if authentication:
        response = JSONResponse(content="User Authenticated")
        response.set_cookie(
            key="jwt",
            value=authentication["token"],
            httponly=True,
            max_age=os.environ['JWT_EXPIRATION_TIME'],
            secure=True,
            samesite="strict"
        )
        return response
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    

@app.post("/users/validate_token/")
async def validate_jwt_endpoint(token: JWToken):
    """
    Validates the jwt token
    """
