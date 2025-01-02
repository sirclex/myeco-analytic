from typing import Any
from sqlalchemy.orm import Session

import crud
from schemas.dim_identity import DimIdentityCreate

def create_identity(db: Session, identity_in: DimIdentityCreate) -> Any:
    identity = crud.dim_identity.create(db, obj_in=identity_in)
    return identity