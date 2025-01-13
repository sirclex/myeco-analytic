from fastapi import APIRouter

from api.v1 import fact_debts, fact_transactions

api_router = APIRouter()
api_router.include_router(fact_debts.router, prefix="/debt", tags=["fact_debts"])
api_router.include_router(fact_transactions.router, prefix="/transaction", tags=["fact_transactions"])