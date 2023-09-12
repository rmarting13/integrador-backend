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

    def __str__(self):
        return f""" 
                server_id: {self.server_id}
                name: {self.name}
                description: {self.description}
                icon: {self.icon}
            """
    
    @classmethod
    def create_server(cls, serv):
        """create a new server
        """
        query = "INSERT INTO servers (name, description) VALUES (%s, %s, %s)"
        params = serv.name, serv.description
        db.execute_query(query=query, params=params)


