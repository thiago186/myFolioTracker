"""
    This file contains the classes that represent the tables in the database.
"""
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime
from enum import Enum  

from sqlmodel import Field, SQLModel


class UUIDModel(SQLModel):
    """Base class for all models that use UUID as primary key"""
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False
        )


class TimestampModel(SQLModel):
    """Base class for all models that use timestamps"""
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )


class UserBase(SQLModel):
    """Base class for all user models"""
    username:str = Field(nullable=False)
    email:str = Field(
        unique=True,
        nullable=False
    )
    hashed_password: str
    last_login: Optional[datetime] = None
    is_active: bool = True
    is_admin: bool = False
    role: str= 'common'


class Users(UserBase, UUIDModel, TimestampModel, table=True):
    """Class that represents the users table in the database"""


class AssetType(str, Enum):
    acao = "acao"
    fii = "fii"
    fundos = "fundos"
    bond = "bond"
    option = "option"
    stock = "stock"
    custom = "custom"


class TransactionType(str, Enum):
    """Class that represents the transaction types"""
    buy = "buy"
    sell = "sell"

class TransactionsTable(SQLModel, table=True):
    """
    Base class for all transactions models

    id - transaction id
    ticker - asset ticker
    asset_type - asset type
    buy_date - date of the buy/sell transaction
    due_date - due date of the transaction
    broker - broker used for the transaction
    transaction_type - buy or sell
    price - price of the asset
    quantity - quantity of the asset
    costs - costs associated to the transaction (broker fees, taxes, etc)
    total_price - total price of the transaction
    currency - currency used for the transaction
    transaction_source - source of the transaction
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: UUID = Field(
        nullable=False,
        foreign_key=Users.id
    )
    ticker:str = Field(nullable=False)
    asset_type:str = Field(nullable=False)
    buy_date:datetime = Field(nullable=False)
    due_date:datetime = Field(nullable=False)
    broker:str = Field(nullable=False)
    transaction_type:TransactionType = Field(nullable=False)
    price:float = Field(nullable=False)
    quantity:float = Field(nullable=False)
    costs:float = Field(nullable=False)
    total_costs:float = Field(nullable=False)
    currency:str = Field(nullable=False)
    transaction_source:str = Field(nullable=False)
