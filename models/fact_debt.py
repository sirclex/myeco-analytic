from sqlalchemy import Column, Integer, Float, Boolean

from database.base_class import Base

class FactDebt(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer)
    is_income = Column(Boolean)
    identity_id = Column(Integer)
    status_id = Column(Integer)
    amount = Column(Float)