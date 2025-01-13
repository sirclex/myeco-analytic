from sqlalchemy import func, extract
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.fact_transaction import FactTransaction
from models.dim_status import DimStatus
from models.dim_subcategory import DimSubcategory
from schemas import FactTransactionCreate, FactTransactionUpdate


class CRUDFactTransaction(CRUDBase[FactTransaction, FactTransactionCreate, FactTransactionUpdate]):
    def get_sum_transaction_by_month(self, db: Session):
        subquery_status = db.query(DimStatus.id).filter(DimStatus.name == 'Done').subquery()
        subquery_subcategory = db.query(DimSubcategory.id).filter(DimSubcategory.name == 'Switch').subquery()

        return db.query(
            extract('year', FactTransaction.issue_at).label('year'),
            extract('month', FactTransaction.issue_at).label('month'),
            FactTransaction.is_income,
            func.sum(FactTransaction.amount).label('total')
        ).filter(
            FactTransaction.status_id.in_(subquery_status),
            FactTransaction.subcategory_id.notin_(subquery_subcategory)
        ).group_by(
            extract('year', FactTransaction.issue_at),
            extract('month', FactTransaction.issue_at),
            FactTransaction.is_income
        ).order_by(
            extract('year', FactTransaction.issue_at),
            extract('month', FactTransaction.issue_at),
            FactTransaction.is_income
        )


fact_transaction = CRUDFactTransaction(FactTransaction)
