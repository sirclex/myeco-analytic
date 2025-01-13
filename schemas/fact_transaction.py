from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class FactTransactionBase(BaseModel):
    issue_at: Optional[datetime] = None
    wallet_id: Optional[int] = None
    category_id: Optional[int] = None
    subcategory_id: Optional[int] = None
    status_id: Optional[int] = None
    is_income: Optional[bool] = None
    amount: Optional[float] = None

class FactTransactionCreate(FactTransactionBase):
    issue_at: datetime
    wallet_id: int
    category_id: int
    subcategory_id: int
    status_id: int
    is_income: bool
    amount: float

class FactTransactionUpdate(FactTransactionBase):
    id: int

class FactTransactionResponse(FactTransactionBase):
    id: Optional[int]
    wallet: Optional[str]
    category: Optional[str]
    subcategory: Optional[str]
    status: Optional[str]
    class Config:
        from_attributes = True

class TransactionSummaryResponse:
    year: int
    month: int
    is_income: bool
    total: float
