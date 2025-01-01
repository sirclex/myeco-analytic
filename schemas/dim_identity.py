from typing import Optional
from pydantic import BaseModel

class DimIdentityBase(BaseModel):
    name: Optional[str]

class DimIdentityCreate(DimIdentityBase):
    name: str

class DimIdentityUpdate(DimIdentityBase):
    id: int