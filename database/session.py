from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core import settings

engine = create_engine(settings.ANALYTIC_DATABASE_URL, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)