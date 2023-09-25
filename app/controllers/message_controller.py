from flask import request, session
from ..models.message import Message


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
        return {'error': 'Source not found'}, 404

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
        return {'error': 'Source not found'}, 404

    @classmethod
    def create(cls):
        """
        Creates a new message resource
        :return: A Flask Response object
        """
        data = request.json
        message_id = Message.create(Message(**data))
        print(message_id)
        msg = Message.get(Message(message_id=message_id))
        print(msg)
        return vars(msg), 201

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
