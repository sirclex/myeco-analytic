from typing import Any
from sqlalchemy.orm import Session

import crud
from schemas.dim_subcategory import DimSubcategoryCreate

def create_subcategory(db: Session, subcategory_in: DimSubcategoryCreate) -> Any:
    subcategory = crud.dim_subcategory.create(db, obj_in=subcategory_in)
    return subcategory