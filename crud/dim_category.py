from sqlalchemy import func, case
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.dim_category import DimCategory
from schemas import DimCategoryCreate, DimCategoryUpdate


class CRUDDimCategory(CRUDBase[DimCategory, DimCategoryCreate, DimCategoryUpdate]):
    pass


dim_category = CRUDDimCategory(DimCategory)
