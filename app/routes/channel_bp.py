from app.controllers.channel_controller import ChannelController
from flask import Blueprint

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/channels', methods=['POST'])(ChannelController.create)
channel_bp.route('/channels', methods=['GET'])(ChannelController.get_all)
channel_bp.route('/channels/<int:channel_id>', methods=['GET'])(ChannelController.get)
channel_bp.route('/channels/<int:channel_id>', methods=['PUT'])(ChannelController.update)
channel_bp.route('/channels/<int:channel_id>', methods=['DELETE'])(ChannelController.delete)