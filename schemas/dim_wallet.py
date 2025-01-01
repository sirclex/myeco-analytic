from typing import Optional
from pydantic import BaseModel

class DimWalletBase(BaseModel):
    name: Optional[str]

class DimWalletCreate(DimWalletBase):
    name: str

class DimWalletUpdate(DimWalletBase):
    id: int