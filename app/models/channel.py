from app.database import DatabaseConnection as db

class Channel:
    """
    A class which represents a Channels data model
    """
     
    def __init__(self,channel_id=None, server_id=None, user_id=None, name=None, description=None,creation_date=None):
        """
        :param channel_id: (``int``)
        :param server_id: (``int``)
        :param name (``str``)
        :param description (``str``)
        :param creation_date (``datetime``)
        """
        self.channel_id = channel_id
        self.server_id = server_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.creation_date = creation_date

    def serialize (self):
        """
        Serealize object respresentation
        returns: dict
        note: the creation_date is converted to string
        """
        return {
            "channel_id": self.channel_id,
            "server_id": self.server_id,
            "name": self.name,
            "description": self.description,
            "creation_date": str(self.creation_date)
        }

    @classmethod
    def create_channel (cls, chan):
        """create a new channel
           :param chan: An instance of Channel
           :return: None
        """
        query = "INSERT INTO channels (server_id, user_id, name, description) VALUES (%s, %s, %s, %s);"
        params = chan.server_id, chan.user_id, chan.name, chan.description
        return db.execute_query(query=query, params=params)
    
    @classmethod
    def get_channel(cls, chan):
        """Gets the channel model entry in database that matches the channel_id provided 
           :param chan: An instance of channel
           :return: None or Channel
        """
        attrs = vars(chan).keys()
        query = f"SELECT {', '.join(attrs)} FROM channels WHERE channel_id= %s;"
        params = chan.channel_id,
        result = db.fetch_one(query=query, params=params)
        if result:
            items = list(zip(attrs, result))
            kwargs = {}
            for key, value in items:
                kwargs.update({key: value})
            return cls(*result)
        return None
    
    @classmethod
    def get_all_channel(cls, chan=None):
        """
        Gets a collection of all Channel entries existing in the database or
        those that matches channel's data provided by param
        :return: A Channel list or None
        """
        attrs = vars(Channel()).keys()
        if chan:
            query_parts = []
            params = []
            for key, value in vars(chan).items():
                if value:
                    query_parts.append(key)
                    params.append('%'+value+'%')
            if len(query_parts) > 1:
                query = (f"SELECT {', '.join(attrs)} FROM channels WHERE {query_parts.pop(0)}" +
                         ' LIKE %s AND '.join(query_parts) + ";")
            else:
                query = f"SELECT {', '.join(attrs)} FROM channels WHERE {query_parts.pop()} LIKE %s;"
            result = db.fetch_all(query=query, params=params)
        else:
            query = f"SELECT {', '.join(attrs)} FROM channels;"
            result = db.fetch_all(query=query)
        if result:
            channels = []
            for row in result:
                kwargs = {}
                for key, value in zip(attrs, row):
                    kwargs.update({key: value})
                channels.append(cls(**kwargs))
            return channels
        else:
            return None
    
    @classmethod
    def update_channel(cls, chan):
        """
        Updates the values of the Channel model entry in the database that matches the channel_id provided
        :param chan: An instance of Channel
        :return: None
        """
        allowed_columns = {'name', 'description'}
        query_parts = []
        params = []
        for key, value in vars(chan).items():
            if key in allowed_columns and value:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(chan.channel_id)
        query = "UPDATE channels SET " + ", ".join(query_parts) + " WHERE channel_id = %s;"
        db.execute_query(query, params=params)
    
    @classmethod
    def delete_channel(cls, chan):
        """
        Deletes the Channel model entry in the database that matches the channel_id provided
        :param chan: An instance of Channel
        :return: None
        """
        query = "DELETE FROM channels WHERE channel_id = %s;"
        param = chan.channel_id,
        db.execute_query(query=query, params=param)

    
    @classmethod
    def filtrar_channel(cls, chan):
        """
        :param chan: An instance of channel
        :return: None or list of Channel
        """
        query = "SELECT channel_id, server_id, name, description, creation_date FROM channels WHERE name LIKE %s"
        nam = chan.name,
        param = f"%{nam}%"
        result = db.fetch_all(query=query, params=param)
        if result:
            return result
        else: 
            return None 
    
    @classmethod
    def get_all_channel_ofServer(cls, chan):
        """
        
        :param chan: An instance of channel
        :return: None or list of Channel
        """
        attrs = vars(Channel()).keys()
        query = f"SELECT {', '.join(attrs)} FROM channels WHERE server_id = %s;"
        params = chan.server_id
        result = db.fetch_all(query=query, params=params)
        if result:
            return result
        return None

    

    