from flask import request
from ..models.channel import Channel

class ChannelController:
    """Channel controller class that binds user resource requests to user data model. """
    @classmethod
    def create (cls):
        """
        Creates a new channel resource
        :return: A flask response object
        """
        data = request.json
        Channel.create_channel(Channel(**data))
        return {'message': 'Channel created successfully'}, 201

    @classmethod
    def get (cls, channel_id):
        """
        Gets a channel by id
        :param channel_id: (´´int´´)
        :return: A Flask Response object
        """
        chan = Channel(channel_id=channel_id)
        result = Channel.get_channel(chan)
        if result:
            return chan.serialize(), 200
        return {'error': 'Source not found'}, 404

    @classmethod
    def get_all (cls):
        """
        Gets all channels resources
        :return: A Flask Response object
        """
        data = request.args
        if data: 
            result = Channel.get_all_channel(Channel(**data))
        else: 
            result = Channel.get_all_channel()
        if result:
            return list(map(lambda u: vars(u), result)), 200
        return {'error': 'Source not found'}, 404

    @classmethod
    def update (cls, channel_id):
        """
        Updates a channel resource by id
        :param channel_id: (´´int´´)
        :return: A Flask Response object
        """
        data = request.json
        data['channel_id'] = channel_id
        chan = Channel(**data)
        Channel.update_channel(chan)
        return {'message': 'Channel updated successfully'}, 200
    @classmethod
    def delete (cls, channel_id):
        """
        Deletes a channel resource by id
        :param channel_id: (´´int´´)
        :return: A Flask Response object
        """
        chan = Channel(channel_id=channel_id)
        Channel.delete_channel(chan)
        return {}, 204