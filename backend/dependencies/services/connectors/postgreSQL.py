from typing import Optional

from sqlmodel import create_engine, SQLModel


from dependencies.models.users import Users

from dotenv import load_dotenv
import os
load_dotenv()

POSTGRESQL_URL = f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOSTNAME"]}:{os.environ["POSTGRES_PORT"]}/{os.environ["POSTGRES_DB"]}'
