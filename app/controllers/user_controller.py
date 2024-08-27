from flask import jsonify, request
from http import HTTPStatus
from ..services.user_services import create_user, get_all_users


def create_new_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    new_user = create_user(username, email, password)
    return jsonify({"msj": "Usuario creado", "user": new_user.username}), HTTPStatus.CREATED

def list_users():
    users = get_all_users()
    return jsonify([user.username for user in users]), HTTPStatus.ACCEPTED