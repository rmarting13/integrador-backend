from app.controllers.message_controller import MessageController
from flask import Blueprint


message_bp = Blueprint('message_bp', __name__)

message_bp.route('/messages', methods=['POST'])(MessageController.create)
message_bp.route('/messages', methods=['GET'])(MessageController.get_all)
message_bp.route('/messages/<int:message_id>', methods=['GET'])(MessageController.get)
message_bp.route('/messages/<int:message_id>', methods=['PUT'])(MessageController.update)
message_bp.route('/messages/<int:message_id>', methods=['DELETE'])(MessageController.delete)
message_bp.route('/messages/channel/<int:channel_id>', methods=['GET'])(MessageController.get_all_messages_channel)

