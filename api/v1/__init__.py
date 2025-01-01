from fastapi import APIRouter

from api.v1 import fact_debts

api_router = APIRouter()
api_router.include_router(fact_debts.router, prefix="/debt", tags=["fact_debts"])