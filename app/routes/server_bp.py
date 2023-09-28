from app.controllers.server_controller import ServerController
from flask import Blueprint

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/servers', methods=['POST'])(ServerController.create)
server_bp.route('/servers', methods=['GET'])(ServerController.get_all)
server_bp.route('/servers/<int:server_id>', methods=['GET'])(ServerController.get)
server_bp.route('/servers/<int:server_id>', methods=['PUT'])(ServerController.update)
server_bp.route('/servers/<int:server_id>', methods=['DELETE'])(ServerController.delete)
server_bp.route('/servers/filter/name', methods=['GET'])(ServerController.filter_server)
server_bp.route('/servers/user', methods=['GET'])(ServerController.get_all_server_ofUser)
server_bp.route('/servers/user', methods=['POST'])(ServerController.join)
server_bp.route('/servers/user/<int:server_id>', methods=['DELETE'])(ServerController.left)
