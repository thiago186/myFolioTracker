"""
Module for PostgreSQL related operations.
"""
import os
from sqlmodel import create_engine, SQLModel, Session, select
from dotenv import load_dotenv


from dependencies.models.users import UserToRegister
from dependencies.services.connectors.db_table_models import Users
from dependencies.utils.hash import encrypt_field, verify_field


load_dotenv()


POSTGRESQL_URL = (
    f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}'
    f'@{os.environ["POSTGRES_HOSTNAME"]}:{os.environ["POSTGRES_PORT"]}'
    f'/{os.environ["POSTGRES_DB"]}'
)

engine = create_engine(POSTGRESQL_URL, echo=os.environ["SQL_ECHO"].lower()=="true")

async def reset_tables(password):
    """
    Reset all the tables in the database. This function is only available for the admin user.
    """
    if verify_field(password, os.environ["USERS_RESET_PASSWORD_ENCRYPTED"]):
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
    else:
        print("You don't have permission to do this. Users will not be reseted.")


async def register_user(user_infos: UserToRegister):
    """
    Resgister a new user in the database.
    """
    print("function called!")
    user = Users(
        username=user_infos.username,
        email=user_infos.email,
        hashed_password=user_infos.hashed_password,
        last_login=user_infos.last_login,
        is_active=user_infos.is_active,
        is_admin=user_infos.is_admin,
        role=user_infos.role,
    )
    with Session(engine) as session:
        session.add(user)
        session.commit()

async def get_user_by_email(email):
    """
    Get a user by its email.
    """
    with Session(engine) as session:
        statement = select(Users).where(Users.email == email)
        users = session.exec(statement)
        return users.first()