from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class FactDebtBase(BaseModel):
    transaction_id: Optional[int] = None
    is_income: Optional[bool] = None
    identity_id: Optional[int] = None
    status_id: Optional[int] = None
    amount: Optional[float] = None

class FactDebtCreate(FactDebtBase):
    transaction_id: int
    is_income: bool
    identity_id: int
    status_id: int
    amount: float

class FactDebtUpdate(FactDebtBase):
    id: int

class PendingDebtResponse(BaseModel):
    identity: Optional[str] = None
    amount: Optional[float] = None
    class Config:
        from_attributes = True

class FactDebtResponse(FactDebtBase):
    id: Optional[int]
    issue_at: Optional[datetime] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
    identity: Optional[str] = None
    status: Optional[str] = None
    class Config:
        from_attributes = True
