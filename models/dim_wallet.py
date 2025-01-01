from sqlalchemy import Column, Integer, String

from database.base_class import Base

class DimWallet(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    provider = Column(String(32), nullable=False)
    number = Column(String(128))