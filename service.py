from models import User, Offer, Order
from config import db
import json


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get("id"),
                first_name=row.get("first_name"),
                last_name=row.get("last_name"),
                age=row.get("age"),
                email=row.get("email"),
                role=row.get("role"),
                phone=row.get("phone")
            )
        )

    db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get("id"),
                name=row.get("name"),
                description=row.get("description"),
                start_date=row.get("start_date"),
                end_date=row.get("end_date"),
                address=row.get("address"),
                price=row.get("price"),
                customer_id=row.get("customer_id"),
                executor_id=row.get("executor_id")
            )
        )

    db.session.commit()


def insert_data_offer(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get("id"),
                order_id=row.get("order_id"),
                executor_id=row.get("executor_id")
            )
        )

    db.session.commit()


def get_data_users():
    result = []
    for row in User.query.all():
        result.append(row.to_dict())

    return list(result)


def get_data_orders():
    result = []
    for row in Order.query.all():
        result.append(row.to_dict())

    return result


def get_order_by_id(uid):
    try:
        return Order.query.get(uid).to_dict()
    except Exception:
        return {}


def get_all(model):
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())

    return result


def get_all_by_id(model, uid):
    try:
        return model.query.get(uid).to_dict()
    except Exception:
        return {}


def update_data(model, uid, values):
    try:
        db.session.query(model).filter(model.id == uid).update(values)
        db.session.commit()
    except Exception:
        return {}


def delete_data(model, uid):
    try:
        db.session.query(model).filter(model.id == uid).delete()
        db.session.commit()
    except Exception:
        return {}


def init_db():
    db.drop_all()
    db.create_all()

    with open("data/user.json") as file:
        data = json.load(file)
        insert_data_user(data)

    with open("data/order.json") as file:
        data = json.load(file)
        insert_data_order(data)

    with open("data/offer.json") as file:
        data = json.load(file)
        insert_data_offer(data)
