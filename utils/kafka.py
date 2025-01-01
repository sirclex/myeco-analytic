from kafka import KafkaConsumer

from core.config import settings
from constants import kafka_topics

topics = [
    kafka_topics.TRANSACTION_CREATE,
    kafka_topics.TRANSACTION_UPDATE,
    kafka_topics.TRANSACTION_UPDATE_MULTI,
    kafka_topics.DEBT_CREATE,
    kafka_topics.DEBT_UPDATE,
    kafka_topics.DEBT_UPDATE_MULTI,
    kafka_topics.CATEGORY_CREATE,
    kafka_topics.CATEGORY_UPDATE,
    kafka_topics.SUBCATEGORY_CREATE,
    kafka_topics.SUBCATEGORY_UPDATE,
    kafka_topics.IDENTITY_CREATE,
    kafka_topics.IDENTITY_UPDATE,
    kafka_topics.WALLET_CREATE,
    kafka_topics.WALLET_UPDATE,
    kafka_topics.STATUS_CREATE,
    kafka_topics.STATUS_UPDATE,
]

consumer = KafkaConsumer(*topics, bootstrap_servers=settings.KAFKA_SERVER)

def kafka_thread(handler):
    for message in consumer:
        handler(message.topic, message.value)