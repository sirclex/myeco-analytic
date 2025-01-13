from typing import Any
from sqlalchemy.orm import Session

import crud
from schemas.dim_category import DimCategoryCreate

def create_category(db: Session, category_in: DimCategoryCreate) -> Any:
    category = crud.dim_category.create(db, obj_in=category_in)
    return category