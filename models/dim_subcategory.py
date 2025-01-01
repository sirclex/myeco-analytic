from sqlalchemy import Column, Integer, String

from database.base_class import Base

class DimSubcategory(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer)
    name = Column(String(32), nullable=False)