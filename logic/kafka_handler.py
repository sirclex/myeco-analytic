import json
from datetime import datetime
from constants import kafka_topics
from database.session import SessionLocal
from logic import fact_debt_logic, fact_transaction_logic

from schemas import FactDebtCreate, FactTransactionCreate

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


def handle_transaction_create(message: str):
    try:
        json_transaction = json.loads(message)
        transaction = FactTransactionCreate(
            issue_at=datetime.fromisoformat(json_transaction["issue_at"]),
            wallet_id=json_transaction["wallet_id"],
            category_id=json_transaction["category_id"],
            subcategory_id=json_transaction["subcategory_id"],
            status_id=json_transaction["status_id"],
            is_income=json_transaction["is_income"],
            amount=json_transaction["amount"],
        )
        db = SessionLocal()
        fact_transaction_logic.create_transaction(db, transaction)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


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
        kafka_topics.TRANSACTION_CREATE: handle_transaction_create,
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
