from flask import session

from app.database import DatabaseConnection as db


class Server:

    """A class which resprsent a Server data model
    """
    def __init__(self, server_id=None, user_id=None, role_id=None, name=None, description=None, creation_date=None, members=1 ):
        """
        :param server_id: (``int``)
        :param name (``str``)
        :param description (``str``)
        :param creation_date (``datetime``)
        :param members (``int``)
        """
        
        self.server_id = server_id
        self.user_id = user_id
        self.role_id = role_id
        self.name = name
        self.description = description
        self.creation_date = creation_date
        self.members = members

    @classmethod
    def create_server(cls, serv):
        """create a new server
           :param serv: An instance of Server
           :return: None
        """
        query = "INSERT INTO servers (name, description) VALUES (%s, %s);"
        params = serv.name, serv.description
        server_id = db.execute_query(query=query, params=params)
        query = 'INSERT INTO user_roles_servers (user_id, server_id, role_id) VALUES (%s, %s, 1);'
        params = serv.user_id, server_id
        db.execute_query(query=query, params=params)
        return server_id

    def serialize(self):
        """
        Serealize object respresentation
        returns: dict
        note: the creation_date is converted to string
        """
        return {
            "server_id": self.server_id,
            "name": self.name,
            "description": self.description,
            "creation_date": str(self.creation_date)
        }
    
    @classmethod
    def get_server_id(cls, serv):
        """Gets the Serve model entry in database that matches the server_id provided 
           :param serv: An instance of Server
           :return: None or Server
        """

        attrs = 'server_id', 'name', 'description', 'creation_date'
        query = f"SELECT {', '.join(attrs)} FROM servers WHERE server_id= %s;"
        params = serv.server_id,
        result = db.fetch_one(query=query, params=params)
        if result:
            items = list(zip(attrs, result))
            kwargs = {}
            for key, value in items:
                kwargs.update({key: value})
            server = cls(**kwargs)
            query = """SELECT COUNT(*) FROM users u INNER JOIN user_roles_servers urs ON u.user_id = urs.user_id 
                    INNER JOIN servers s ON s.server_id = urs.server_id WHERE s.server_id = %s; """
            param = serv.server_id,
            result = db.fetch_one(query=query, params=param)
            server.members = result[0]
            query = """SELECT user_id FROM user_roles_servers WHERE server_id = %s AND role_id = 1;"""
            result = db.fetch_one(query=query, params=param)
            server.user_id = result[0]
            return server
        return None

    @classmethod 
    def get_all_server(cls, serv=None):
        """
        Gets a collection of all Server entries existing in the database or
        those that matches server's data provided by param
        :return: A Server list or None
        """

        attrs = 'server_id', 'name', 'description', 'creation_date'
        if serv:
            query_parts = []
            params = []
            for key, value in vars(serv).items():
                if value:
                    query_parts.append(key)
                    params.append('%'+value+'%')
            if len(query_parts) > 1:
                query = (f"SELECT {', '.join(attrs)} FROM servers WHERE {query_parts.pop(0)}" +
                         ' LIKE %s AND '.join(query_parts) + ";")
            else:
                query = f"SELECT {', '.join(attrs)} FROM servers WHERE {query_parts.pop()} LIKE %s;"
            result = db.fetch_all(query=query, params=params)
        else:
            query = f"SELECT {', '.join(attrs)} FROM servers;"
            result = db.fetch_all(query=query)
        if result:
            servers = []
            for row in result:
                kwargs = {}
                for key, value in zip(attrs, row):
                    kwargs.update({key: value})
                server = cls(**kwargs)
                query = """SELECT COUNT(*) FROM users u INNER JOIN user_roles_servers urs ON u.user_id = urs.user_id 
                        INNER JOIN servers s ON s.server_id = urs.server_id WHERE s.server_id = %s; """
                param = server.server_id,
                result = db.fetch_one(query=query, params=param)
                server.members = result[0]

                query = """SELECT role_id FROM user_roles_servers WHERE server_id = %s AND user_id = %s;"""
                param = server.server_id, session['user_id']
                result = db.fetch_one(query=query, params=param)
                if result:
                    server.role_id = result[0]
                servers.append(server)
                print('MODEL: ', vars(server))
            return servers
        else:
            return None

    @classmethod
    def update_server(cls, serv):
        """
        Updates the values of the Server model entry in the database that matches the server_id provided
        :param serv: An instance of Server
        :return: None
        """
        allowed_columns = {'name', 'description'}
        query_parts = []
        params = []
        for key, value in vars(serv).items():
            if key in allowed_columns and value:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(serv.server_id)
        query = "UPDATE servers SET " + ", ".join(query_parts) + " WHERE server_id = %s;"
        db.execute_query(query, params=params)


    @classmethod
    def delete_server(cls, serv):
        """
        Deletes the Server model entry in the database that matches the server_id provided
        :param serv: An instance of Server
        :return: None
        """
        query = "DELETE FROM servers WHERE server_id = %s;"
        param = serv.server_id,
        db.execute_query(query=query, params=param)

    @classmethod
    def filtrar_server(cls, serv):
        """

        :param serv: An instance of Server
        :return: A Server list or None
        """
        query = "SELECT server_id, name, description, creation_date FROM servers WHERE name LIKE %s"
        nam = serv.name,
        param = f"%{nam}%"
        result = db.fetch_all(query=query,params=param)
        if result:
            return result
        else: 
            return None

    @classmethod
    def get_all_server_ofUser(cls, serv):
        """
        
        :param serv: An instance of Server
        :return: A Server list or None
        """
        attrs = 'server_id', 'name', 'description', 'creation_date'
        query = """SELECT s.server_id, name, description, s.creation_date FROM servers s 
                INNER JOIN user_roles_servers urs ON s.server_id = urs.server_id WHERE user_id = %s;"""
        param = serv.user_id,
        result = db.fetch_all(query=query, params=param)
        if result:
            servers = []
            for row in result:
                kwargs = {}
                for key, value in zip(attrs, row):
                    kwargs.update({key: value})
                server = cls(**kwargs)
                query = """SELECT COUNT(*) FROM users u INNER JOIN user_roles_servers urs ON u.user_id = urs.user_id 
                                    INNER JOIN servers s ON s.server_id = urs.server_id WHERE s.server_id = %s; """
                param = server.server_id,
                result = db.fetch_one(query=query, params=param)
                server.members = result[0]
                query = """SELECT user_id FROM user_roles_servers WHERE server_id = %s AND role_id = 1;"""
                result = db.fetch_one(query=query, params=param)
                server.user_id = result[0]
                servers.append(server)
            return servers
        else:
            return None
        
    @classmethod
    def join_server(cls, serv):
        """
        
        """
        query = 'INSERT INTO user_roles_servers (user_id, server_id, role_id) VALUES (%s, %s, 2);'
        params = serv.user_id, serv.server_id
        db.execute_query(query=query, params=params)

    @classmethod
    def left_server(cls, serv):
        query = 'DELETE FROM user_roles_servers WHERE user_id = %s AND server_id = %s;'
        params = serv.user_id, serv.server_id
        db.execute_query(query=query, params=params)

if __name__ == "__main__":

    Server.get_all_server()
