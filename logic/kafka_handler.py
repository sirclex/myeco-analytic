import json
from constants import kafka_topics
from database.session import SessionLocal
from logic import fact_debt_logic

from schemas import FactDebtCreate

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


def handle_debt_create(message: str):
    try:
        json_debt = json.loads(message)
        debt = FactDebtCreate(
            transaction_id=json_debt["transaction_id"],
            is_income=json_debt["is_income"],
            amount=json_debt["amount"],
            identity_id=json_debt["identity_id"],
            status_id=json_debt["status_id"],
        )
        db = SessionLocal()
        fact_debt_logic.create_debt(db, debt)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


def handle_kafka_messages(topic: str, message: str):
    # TODO: Implement the logic to handle the messages
    handlers = {
        # kafka_topics.TRANSACTION_CREATE,
        # kafka_topics.TRANSACTION_UPDATE,
        # kafka_topics.TRANSACTION_UPDATE_MULTI,
        kafka_topics.DEBT_CREATE: handle_debt_create,
        # kafka_topics.DEBT_UPDATE,
        # kafka_topics.DEBT_UPDATE_MULTI,
        # kafka_topics.CATEGORY_CREATE,
        # kafka_topics.CATEGORY_UPDATE,
        # kafka_topics.SUBCATEGORY_CREATE,
        # kafka_topics.SUBCATEGORY_UPDATE,
        # kafka_topics.IDENTITY_CREATE,
        # kafka_topics.IDENTITY_UPDATE,
        # kafka_topics.WALLET_CREATE,
        # kafka_topics.WALLET_UPDATE,
        # kafka_topics.STATUS_CREATE,
        # kafka_topics.STATUS_UPDATE,
    }

    handler = handlers.get(topic)
    if handler:
        handler(message)
    else:
        print(f"No handler found for topic: {topic}")
