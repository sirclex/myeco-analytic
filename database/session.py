from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import settings
from database.base_class import Base

engine = create_engine(settings.ANALYTIC_DATABASE_URL, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)