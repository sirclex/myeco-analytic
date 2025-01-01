from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import api_router
from core import settings, get_api_key
from utils.kafka import consumer
from logic.kafka_handler import handle_kafka_messages

origins = {settings.ANALYTIC_CORS_ORIGIN}

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)
    
app.include_router(api_router, prefix="/myeco/analytic", dependencies=[Security(get_api_key)])

for message in consumer:
    handle_kafka_messages(message.topic, message.value)