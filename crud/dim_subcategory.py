from sqlalchemy import func, case
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.dim_subcategory import DimSubcategory
from schemas import DimSubcategoryCreate, DimSubcategoryUpdate

class CRUDDimSubcategory(CRUDBase[DimSubcategory, DimSubcategoryCreate, DimSubcategoryUpdate]):
    pass


dim_subcategory = CRUDDimSubcategory(DimSubcategory)
