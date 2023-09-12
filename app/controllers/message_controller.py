from flask import request
from ..models.message import Message


class MessageController:
    """Message controller class that binds message resource requests to message data model."""

    @classmethod
    def get(cls, message_id):
        """
        Gets a message by id
        :param message_id: (´´int´´)
        :return: A Flask Response object
        """
        message = Message(message_id=message_id)
        result = Message.get(message)
        if result:
            return vars(result), 200
        else:
            return {'error': 'Source not found'}, 404

    @classmethod
    def get_all(cls):
        """
        Gets all message resources
        :return: A Flask Response object
        """
        result = Message.get_all()
        if result:
            messages = []
            for row in result:
                messages.append(vars(row))
            return messages, 200
        else:
            return {'error': 'Source not found'}, 404

    @classmethod
    def create(cls):
        """
        Creates a new message resource
        :return: A Flask Response object
        """
        data = request.json
        Message.create(Message(**data))
        return {'message': 'Message created successfully'}, 201

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
        return {}, 200

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
