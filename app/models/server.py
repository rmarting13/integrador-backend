from app.database import DatabaseConnection as db

class Server:

    """A class which resprsent a Server data model
    """
    def __init__(self, server_id=None, name=None, description=None, icon=None, creation_date=None ):
        """
        :param server_id: (``int``)
        :param name (``str``)
        :param description (``str``)
        :param icon (``str``)
        :param creation_date (``datetime``)
        """
        
        
        self.server_id = server_id
        self.name = name
        self.description = description
        self.icon = icon
        self.creation_date = creation_date

    
    @classmethod
    def create_server(cls, serv):
        """create a new server
           :param serv: An instance of Server
           :return: None
        """
        query = "INSERT INTO servers (name, description) VALUES (%s, %s);"
        params = serv.name, serv.description
        db.execute_query(query=query, params=params)

    def serialize (self):
        """
        Serealize object respresentation
        returns: dict
        note: the creation_date is converted to string
        """
        return {
            "server_id": self.server_id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "creation_date": str(self.creation_date)
        }
    
    @classmethod
    def get_server_id (cls, serv):
        """Gets the Serve model entry in database that matches the server_id provided 
           :param serv: An instance of Server
           :return: None or Server
        """
        attrs = vars(serv).keys()
        query = f"SELECT {', '.join(attrs)} FROM servers WHERE server_id= %s;"
        params = serv.server_id,
        result = db.fetch_one (query=query, params=params)
        if result:
            items = list(zip(attrs, result))
            kwargs = {}
            for key, value in items:
                kwargs.update({key: value})
            return cls(*result)
        else: return None

    @classmethod 
    def get_all_server(cls, serv=None):
        """
        Gets a collection of all Server entries existing in the database or
        those that matches server's data provided by param
        :return: A Server list or None
        """
        attrs = vars(Server()).keys()
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
                servers.append(cls(**kwargs))
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
        allowed_columns = {'name', 'description', 'icon'}
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
    def filtrar_server(cls, nam):
        """

        """
        pass

    @classmethod
    def get_all_server_ofUser(cls, user_id):
        """
        
        """
        query = "SELECT * FROM servers WHERE server_id IN (SELECT server_id FROM user_roles_servers WHERE user_id = %s);"
        result = db.fetch_all(query=query, params=user_id)
        if result:
            return result
        else:
            return None