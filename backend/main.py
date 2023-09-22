import os
# import jwt
import logging


from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from dependencies.utils.hashing import encrypt_password, verify_password
from dependencies.models.users.users import UserToRegister
from dependencies.services.connectors.postgres_sql import register_user

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

@app.post("/hello/")
async def hello_endpoint():
    return {"hello": "world"}


@app.post("/users/register_user/")
async def register_user_endpoint(user: UserToRegister):
    print(f"received user: {user}")
    logging.debug(f'Received user: {user}')
    user.hashed_password = encrypt_password(user.password)
    logging.debug("Password encrypted")
    try: 
        await register_user(user)
        return {"status_code": 201, "detail": "User created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
