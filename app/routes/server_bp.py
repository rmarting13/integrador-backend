from app.controllers.server_controller import ServerController
from flask import Blueprint

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/servers', methods=['POST'])(ServerController.create)
server_bp.route('/servers', methods=['GET'])(ServerController.get_all)
server_bp.route('/servers/<int:server_id>', methods=['GET'])(ServerController.get)
server_bp.route('/servers/<int:server_id>', methods=['PUT'])(ServerController.update)
server_bp.route('/servers/<int:server_id>', methods=['DELETE'])(ServerController.delete)
server_bp.route('/servers/', methods=['GET'])(ServerController.filtrer_server)
server_bp.route('/servers/', methods=['GET'])(ServerController.get_all_server_ofUser)

