from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.fact_transaction import TransactionSummaryResponse, DistributedResponse
from logic import fact_transaction_logic
from api.deps import get_db

router = APIRouter()

@router.get("/sumbymonth", response_model=List[TransactionSummaryResponse])
def get_sum_transaction_by_month(db: Session = Depends(get_db)) -> Any:
    return fact_transaction_logic.get_sum_transaction_by_month(db)

@router.get("/distributedcurrent", response_model=List[DistributedResponse])
def get_category_distributed_by_current_month(db: Session = Depends(get_db)) -> Any:
    return fact_transaction_logic.get_category_distributed_by_current_month(db)