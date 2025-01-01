from typing import Optional
from pydantic import BaseModel

class DimSubcategoryBase(BaseModel):
    name: Optional[str]
    category_id: Optional[int]

class DimSubcategoryCreate(DimSubcategoryBase):
    name: str
    category_id: int

class DimSubcategoryUpdate(DimSubcategoryBase):
    id: int