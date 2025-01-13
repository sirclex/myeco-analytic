from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.fact_debt import PendingDebtResponse
from logic import fact_debt_logic
from api.deps import get_db

router = APIRouter()

@router.get("/pending", response_model=List[PendingDebtResponse])
def get_pending_debts(db: Session = Depends(get_db)) -> Any:
    return fact_debt_logic.get_pending_debts(db)