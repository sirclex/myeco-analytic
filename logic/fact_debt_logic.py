from typing import Any
from sqlalchemy.orm import Session

import crud
from schemas.fact_debt import FactDebtCreate

def get_pending_debts(db: Session) -> Any:
    debts = crud.fact_debt.get_pending_debts(db)
    return debts

def create_debt(db: Session, debt_in: FactDebtCreate) -> Any:
    debt = crud.fact_debt.create(db, obj_in=debt_in)
    return debt