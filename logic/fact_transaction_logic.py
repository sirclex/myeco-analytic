from typing import Any
from sqlalchemy.orm import Session

import crud
from schemas.fact_transaction import FactTransactionCreate

def create_transaction(db: Session, transaction_in: FactTransactionCreate) -> Any:
    transaction = crud.fact_transaction.create(db, obj_in=transaction_in)
    return transaction