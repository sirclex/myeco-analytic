from sqlalchemy import func, case
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.dim_identity import DimIdentity
from schemas import DimIdentityCreate, DimIdentityUpdate


class CRUDDimIdentity(CRUDBase[DimIdentity, DimIdentityCreate, DimIdentityUpdate]):
    pass


dim_identity = CRUDDimIdentity(DimIdentity)
