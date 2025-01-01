from typing import Optional
from pydantic import BaseModel

class DimCategoryBase(BaseModel):
    name: Optional[str]

class DimCategoryCreate(DimCategoryBase):
    name: str

class DimCategoryUpdate(DimCategoryBase):
    id: int