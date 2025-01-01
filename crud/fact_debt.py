from sqlalchemy import func, case
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.fact_debt import FactDebt
from models.dim_identity import DimIdentity
from schemas import FactDebtCreate, FactDebtUpdate


class CRUDFactDebt(CRUDBase[FactDebt, FactDebtCreate, FactDebtUpdate]):
    def get_pending_debts(self, db: Session):
        return (
            db.query(
                DimIdentity.name.label("identity"),
                (
                    func.sum(
                        case((FactDebt.is_income == True, FactDebt.amount), else_=0)
                    )
                    - func.sum(
                        case((FactDebt.is_income == False, FactDebt.amount), else_=0)
                    )
                ).label("amount"),
            )
            .join(DimIdentity, FactDebt.identity_id == DimIdentity.id)
            .filter(FactDebt.status_id == 1)
            .group_by(DimIdentity.name)
            .all()
        )


fact_debt = CRUDFactDebt(FactDebt)
