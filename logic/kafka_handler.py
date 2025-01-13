import json
from datetime import datetime
from constants import kafka_topics
from database.session import SessionLocal
from logic import (
    fact_debt_logic,
    fact_transaction_logic,
    dim_category_logic,
    dim_subcategory_logic,
    dim_identity_logic,
)

from schemas import (
    FactDebtCreate,
    FactDebtUpdate,
    FactTransactionCreate,
    FactTransactionUpdate,
    DimCategoryCreate,
    DimSubcategoryCreate,
    DimIdentityCreate,
)

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


def handle_category_create(message: str):
    try:
        json_category = json.loads(message)
        category = DimCategoryCreate(
            name=json_category["name"],
        )
        db = SessionLocal()
        dim_category_logic.create_category(db, category)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


def handle_subcategory_create(message: str):
    try:
        json_subcategory = json.loads(message)
        subcategory = DimSubcategoryCreate(
            category_id=json_subcategory["category_id"],
            name=json_subcategory["name"],
        )
        db = SessionLocal()
        dim_subcategory_logic.create_subcategory(db, subcategory)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


def handle_identity_create(message: str):
    try:
        json_identity = json.loads(message)
        identity = DimIdentityCreate(
            name=json_identity["name"],
        )
        db = SessionLocal()
        dim_identity_logic.create_identity(db, identity)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


def handle_update_multi_debts(message: str):
    try:
        json_debts = json.loads(message)
        cooked_data = []
        for debt in json_debts:
            cooked_data.append(
                FactDebtUpdate(
                    id=debt["id"],
                    transaction_id=debt["transaction_id"],
                    is_income=debt["is_income"],
                    amount=debt["amount"],
                    identity_id=debt["identity_id"],
                    status_id=debt["status_id"],
                )
            )
        db = SessionLocal()
        fact_debt_logic.update_multi_debts(db, cooked_data)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


def handle_update_multi_transactions(message: str):
    try:
        json_transactions = json.loads(message)
        cooked_data = []
        for transaction in json_transactions:
            cooked_data.append(
                FactTransactionUpdate(
                    id=transaction["id"],
                    issue_at=datetime.fromisoformat(transaction["issue_at"]),
                    wallet_id=transaction["wallet_id"],
                    category_id=transaction["category_id"],
                    subcategory_id=transaction["subcategory_id"],
                    status_id=transaction["status_id"],
                    is_income=transaction["is_income"],
                    amount=transaction["amount"],
                )
            )
        db = SessionLocal()
        fact_transaction_logic.update_multi_transactions(db, cooked_data)
    except json.JSONDecodeError:
        print(f"Invalid JSON: {message}")
    finally:
        db.close()


def handle_kafka_messages(topic: str, message: str):
    # TODO: Implement the logic to handle the messages
    handlers = {
        kafka_topics.TRANSACTION_CREATE: handle_transaction_create,
        # kafka_topics.TRANSACTION_UPDATE,
        kafka_topics.TRANSACTION_UPDATE_MULTI: handle_update_multi_transactions,
        kafka_topics.DEBT_CREATE: handle_debt_create,
        # kafka_topics.DEBT_UPDATE,
        kafka_topics.DEBT_UPDATE_MULTI: handle_update_multi_debts,
        kafka_topics.CATEGORY_CREATE: handle_category_create,
        # kafka_topics.CATEGORY_UPDATE,
        kafka_topics.SUBCATEGORY_CREATE: handle_subcategory_create,
        # kafka_topics.SUBCATEGORY_UPDATE,
        kafka_topics.IDENTITY_CREATE: handle_identity_create,
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
