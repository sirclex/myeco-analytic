from sqlalchemy import Column, Integer, String

from database.base_class import Base

class DimIdentity(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)