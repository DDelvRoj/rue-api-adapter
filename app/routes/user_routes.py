from flask import Blueprint

from ..controllers.user_controller import (
    create_new_user,
    list_users
)


user_bp = Blueprint('/user_bp',__name__)

user_bp.route('/users', methods=['POST'])(create_new_user)
user_bp.route('/users/all', methods=['GET'])(list_users)