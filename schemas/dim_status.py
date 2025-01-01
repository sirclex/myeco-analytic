from typing import Optional
from pydantic import BaseModel

class DimStatusBase(BaseModel):
    name: Optional[str]

class DimStatusCreate(DimStatusBase):
    name: str

class DimStatusUpdate(DimStatusBase):
    id: int