from sqlalchemy import Column, Integer, Float, Boolean, DateTime

from database.base_class import Base

class FactTransaction(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    issue_at = Column(DateTime)
    wallet_id = Column(Integer)
    category_id = Column(Integer)
    subcategory_id = Column(Integer)
    status_id = Column(Integer)
    is_income = Column(Boolean)
    amount = Column(Float)