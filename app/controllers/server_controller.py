from flask import request
from ..models.server import Server

class ServerController:
    """Server controller class that binds user resource requests to user data model """

    @classmethod
    def create (cls):
        """
        Creates a new server resource
        :return: A flask response object
        """
        data = request.json
        Server.create_server(Server(**data))
        return {'message': 'Server created successfully'}, 201
    @classmethod
    def get (cls, server_id):
        """
        Gets a server by id
        :param server_id: (´´int´´)
        :return: A Flask Response object
        """
        server = Server(server_id=server_id)
        result = Server.get_server_id(server)
        if result:
            return server.serialize(), 200
        return {'error': 'Source not found'}, 404
    @classmethod
    def get_all (cls):
        """
        Gets all servers resources
        :return: A Flask Response object
        """
        data = request.args
        if data: 
            result = Server.get_all_server(Server(**data))
        else: 
            result = Server.get_all_server()
        if result:
            return list(map(lambda u: vars(u), result)), 200
        return {'error': 'Source not found'}, 404
    @classmethod
    def update (cls, server_id):
        """
        Updates a server resource by id
        :param server_id: (´´int´´)
        :return: A Flask Response object
        """
        data = request.json
        data['server_id'] = server_id
        server = Server(**data)
        Server.update_server(server)
        return {'message': 'Server updated successfully'}, 200
    @classmethod
    def delete (cls, server_id):
        """
        Deletes a server resource by id
        :param server_id: (´´int´´)
        :return: A Flask Response object
        """
        serv = Server(server_id=server_id)
        Server.delete_server(serv)
        return {}, 204
