from app.controllers.user_controller import UserController
from flask import Blueprint


user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['POST'])(UserController.create)
user_bp.route('/users', methods=['GET'])(UserController.get_all)
user_bp.route('/users/<int:user_id>', methods=['GET'])(UserController.get)
user_bp.route('/users', methods=['PUT'])(UserController.update)
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(UserController.delete)
user_bp.route('/users/login', methods=['POST'])(UserController.login)
user_bp.route('/users/logout', methods=['GET'])(UserController.logout)
user_bp.route('/users/profile', methods=['GET'])(UserController.show_profile)
user_bp.route('/users/pass/<string:pw>', methods=['GET'])(UserController.current_password)

