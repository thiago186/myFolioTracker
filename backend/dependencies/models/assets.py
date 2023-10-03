from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class TransactionType(str, Enum):
    """Class that represents the transaction types"""
    buy = "buy"
    sell = "sell"

class CurrencyType(str, Enum):
    usd = "usd"
    brl = "brl"
    eur = "eur"

class Transaction(BaseModel):
    """
    Base class for all transactions models

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
    transaction_source_id - id for a group of transactions from the same source
    """
    ticker:str = Field(...)
    owner_id:Optional[str]
    asset_type:str = Field(...)
    buy_date:datetime = Field(...)
    due_date:datetime = Field(...)
    broker:str = Field(...)
    transaction_type:TransactionType = Field(...)
    price:float = Field(...)
    quantity:float = Field(...)
    costs:float = Field(...)
    total_cost:Optional[float]
    currency:str = Field(...)
