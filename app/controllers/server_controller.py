from flask import request, session
from ..models.server import Server
from ..models.exceptions import Forbidden, ServerError, BadRequest, NotFound

class ServerController:
    """Server controller class that binds user resource requests to user data model """

    @classmethod
    def create(cls):
        """
        Creates a new server resource
        :return: A flask response object
        """

        data = request.json
        data['user_id'] = session['user_id']
        server_id = Server.create_server(Server(**data))
        return {'server_id': server_id}, 201

    @classmethod
    def get(cls, server_id):
        """
        Gets a server by id
        :param server_id: (´´int´´)
        :return: A Flask Response object
        """
        server = Server(server_id=server_id)
        result = Server.get_server_id(server)
        if result:
            print(vars(result))
            return vars(result), 200
        return NotFound
    
    @classmethod
    def get_all(cls):
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
            # servers = []
            # for reg in result:
            #     if reg.user_id == session['user_id']:
            #         servers.append({
            #             'server': vars(reg),
            #             'status': 1
            #         })
            #     elif :
            #         servers.append({
            #             'server': vars(reg),
            #             'status': False
            #         })
            # return servers, 200
            return list(map(lambda u: vars(u), result)), 200
        return {}, 404
        # return NotFound

    @classmethod
    def update(cls, server_id):
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
    def delete(cls, server_id):
        """
        Deletes a server resource by id
        :param server_id: (´´int´´)
        :return: A Flask Response object
        """
        serv = Server(server_id=server_id)
        Server.delete_server(serv)
        return {}, 204

    @classmethod
    def filter_server(cls, name):
        """
        
        """
        serv = Server(name=name)
        result = Server.filtrar_server(serv)
        if result:
            return result

    @classmethod
    def get_all_server_ofUser(cls):
        """
        
        """
        serv = Server(user_id=session['user_id'])
        result = Server.get_all_server_ofUser(serv)
        if result:
            servers = []
            for reg in result:
                if reg.user_id == session['user_id']:
                    servers.append({'server': vars(reg), 'owner': True})
                else:
                    servers.append({'server': vars(reg), 'owner': False})
            return servers, 200
        else:
            print('FALLA EL ENVIO')
        return {}, 404
        # return NotFound


    @classmethod
    def left(cls, server_id):
        Server.left_server(Server(user_id=session['user_id'], server_id=server_id))
        return {}, 204

    @classmethod
    def join(cls):
        data = request.json
        data['user_id'] = session['user_id']
        Server.join_server(Server(**data))
        return {'message': 'Server joined successfully'}, 201
