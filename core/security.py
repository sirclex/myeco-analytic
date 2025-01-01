from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

from core import settings

api_key_header = APIKeyHeader(name=settings.ANALYTIC_API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == f"Bearer {settings.ANALYTIC_API_KEY}":
        return api_key_header
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")