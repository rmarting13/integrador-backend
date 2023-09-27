from flask import request, session
from ..models.message import Message
from ..models.exceptions import Forbidden, ServerError, BadRequest, NotFound



class MessageController:
    """Message controller class that binds message resource requests to message data model."""

    @classmethod
    def get(cls, message_id):
        """
        Gets a message by id
        :return: A Flask Response object
        """
        message = Message(message_id=message_id)
        result = Message.get(message)
        if result:
            return vars(result), 200
        return NotFound

    @classmethod
    def get_all(cls):
        """
        Gets all message resources
        :return: A Flask Response object
        """
        data = request.args
        if data:
            result = Message.get_all(Message(**data))
        else:
            result = Message.get_all()
        if result:
            messages = []
            for row in result:
                msg = vars(row)
                msg['owner'] = True if row.user_id == session['user_id'] else False
                messages.append(msg)
            return messages, 200
        return NotFound

    @classmethod
    def create(cls):
        """
        Creates a new message resource
        :return: A Flask Response object
        """
        data = request.json
        data['user_id'] = session['user_id']
        message_id = Message.create(Message(**data))
        return {'message_id': message_id}, 201

    @classmethod
    def update(cls, message_id):
        """
        Updates a message resource by id
        :param message_id: (´´int´´)
        :return: A Flask Response object
        """
        data = request.json
        data['message_id'] = message_id
        message = Message(**data)
        Message.update(message)
        return {'message': 'Message updated successfully'}, 200

    @classmethod
    def delete(cls, message_id):
        """
        Deletes a message resource by id
        :param message_id: (´´int´´)
        :return: A Flask Response object
        """
        message = Message(message_id=message_id)
        Message.delete(message)
        return {}, 204

    @classmethod
    def get_all_messages_channel(cls, channel_id):
        """
        
        """
        message = Message(channel_id = channel_id)
        result = Message.get_all_messages_of_channel(message)
        if result:
            return vars(result), 200
        return NotFound