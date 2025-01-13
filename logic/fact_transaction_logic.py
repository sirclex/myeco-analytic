from typing import Any, List
from sqlalchemy.orm import Session

import crud
from schemas.fact_transaction import FactTransactionCreate, FactTransactionUpdate

def create_transaction(db: Session, transaction_in: FactTransactionCreate) -> Any:
    transaction = crud.fact_transaction.create(db, obj_in=transaction_in)
    return transaction

def update_multi_transactions(db: Session, transactions_in: List[FactTransactionUpdate]) -> Any:
    transactions = crud.fact_transaction.update_multi(db, objs_in=transactions_in)
    return transactions

def get_sum_transaction_by_month(db: Session) -> Any:
    result = crud.fact_transaction.get_sum_transaction_by_month(db)
    return result