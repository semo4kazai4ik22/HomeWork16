import json
from flask import request
from config import app
from service import init_db, get_data_users, get_data_orders, get_order_by_id, get_all, get_all_by_id, update_data, \
    insert_data_user, insert_data_offer, insert_data_order, delete_data
from models import Order, Offer, User


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
                response=json.dumps(get_data_users(), indent=4, ensure_ascii=False),
                status=200,
                mimetype="application/json"
            )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print("Не верный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(uid):
    if request.method == 'GET':
        data = get_data_users()

        for row in data:
            if row["id"] == uid:
                return app.response_class(
                    response=json.dumps(row, indent=4, ensure_ascii=False),
                    status=200,
                    mimetype="application/json"
                )
    elif request.method == 'PUT':
        update_data(User, uid, request.json)
        return app.response_class(
            response=json.dumps(["Done"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(User, uid)
        return app.response_class(
            response=json.dumps(["Done"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    return "Нет пользователя с таким id"


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_data_orders(), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_order(request.json)
        elif isinstance(request.json, dict):
            insert_data_order([request.json])
        else:
            print("Не верный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_orders_by_id(uid):
    if request.method == 'GET':
        data = get_order_by_id(uid)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data(Order, uid, request.json)
        return app.response_class(
            response=json.dumps(["Done"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(Order, uid)
        return app.response_class(
            response=json.dumps(["Done"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=['GET', 'POST'])
def get_all_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_offer(request.json)
        elif isinstance(request.json, dict):
            insert_data_offer([request.json])
        else:
            print("Не верный тип данных")

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:uid>", methods=['GET', 'PUT', 'DELETE'])
def get_offers_by_id(uid):
    if request.method == 'GET':
        data = get_all_by_id(Offer, uid)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_data(Offer, uid, request.json)
        return app.response_class(
            response=json.dumps(["Done"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_data(Offer, uid)
        return app.response_class(
            response=json.dumps(["Done"], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(port=8080, debug=True)
