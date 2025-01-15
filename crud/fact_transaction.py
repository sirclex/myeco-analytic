from sqlalchemy import func, extract
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.fact_transaction import FactTransaction
from models.dim_status import DimStatus
from models.dim_category import DimCategory
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
    
    def get_distributed_by_category(self, db: Session, month: int):
        # select extract(year from issue_at) as year, extract(month from issue_at) as month,
        # dimcategory.name,
        # sum(facttransaction.amount)
        # from facttransaction
        # join dimcategory on facttransaction.category_id = dimcategory.id
        # where status_id in (select id from dimstatus where name = 'Done')
        # and subcategory_id not in (select id from dimsubcategory where name = 'Switch')
        # and is_income = False
        # and extract(month from issue_at) = extract(month from current_timestamp)
        # group by year, month, dimcategory.name
        # order by year, month, dimcategory.name
        subquery_status = db.query(DimStatus.id).filter(DimStatus.name == 'Done').subquery()
        subquery_subcategory = db.query(DimSubcategory.id).filter(DimSubcategory.name == 'Switch').subquery()

        return db.query(
            extract('year', FactTransaction.issue_at).label('year'),
            extract('month', FactTransaction.issue_at).label('month'),
            DimCategory.name,
            func.sum(FactTransaction.amount).label('total')
        ).join(
            DimCategory, FactTransaction.category_id == DimCategory.id
        ).filter(
            FactTransaction.status_id.in_(subquery_status),
            FactTransaction.subcategory_id.notin_(subquery_subcategory),
            FactTransaction.is_income == False,
            extract('month', FactTransaction.issue_at) == month
        ).group_by(
            extract('year', FactTransaction.issue_at).label('year'),
            extract('month', FactTransaction.issue_at).label('month'),
            DimCategory.name
        ).order_by(
            extract('year', FactTransaction.issue_at).label('year'),
            extract('month', FactTransaction.issue_at).label('month'),
            DimCategory.name
        )


fact_transaction = CRUDFactTransaction(FactTransaction)
