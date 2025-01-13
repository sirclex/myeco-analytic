from crud.base import CRUDBase
from models.fact_transaction import FactTransaction
from schemas import FactTransactionCreate, FactTransactionUpdate


class CRUDFactTransaction(CRUDBase[FactTransaction, FactTransactionCreate, FactTransactionUpdate]):
    pass


fact_transaction = CRUDFactTransaction(FactTransaction)
