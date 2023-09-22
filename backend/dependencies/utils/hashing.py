import bcrypt
import os
from dotenv import load_dotenv
load_dotenv()

def encrypt_password(password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), os.environ["CONSTANT_SALT"].encode('utf-8'))
    return hashed_password.decode('utf-8')