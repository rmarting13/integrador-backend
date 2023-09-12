from app.database import DatabaseConnection as db


class Channel:
    """
    A class which represents a channel's data model
    """
    def __init__(self, channel_id=None, server_id=None, name=None, description=None, creation_date=None):
        """

        :param channel_id: (``int``)
        :param server_id: (``int``)
        :param name: (``str``)
        :param description: (``str``)
        :param creation_date: (``datetime``)
        """
        self.channel_id = channel_id
        self.server_id = server_id
        self.name = name
        self.description = description
        self.creation_date = creation_date

    def __str__(self):
        """
        :return : A string representation of the channel data object
        """
        return f"""
                channel_id: {self.channel_id}
                server_id: {self.server_id}
                name: {self.name}
                description: {self.description}
                creation_date: {self.creation_date}
                """

    @classmethod
    def get(cls, channel):
        """
        Gets the Channel model entry in database that matches the channel_id provided
        :param channel: An instance of Channel with a not null channel_id
        :return: Channel or None
        """
        pass

    @classmethod
    def get_all(cls):
        """
        Gets a collection of all Channel objects existing in database
        :return: A Channel list or None
        """
        pass

    @classmethod
    def get_by_name(cls, channel):
        """
        Gets all Channels from database that matches the provided channel name
        :param channel: An instance of Channel with a not null name
        :return: A Channel list or None
        """
        pass

    @classmethod
    def create(cls, channel):
        """
        Creates a new Channel model entry in the database
        :param channel: An instance of Channel
        :return: None
        """
        pass

    @classmethod
    def update(cls, channel):
        """
        Updates the values of the Channel model entry in the database that matches the channel_id provided
        :param channel: An instance of Channel
        :return: None
        """
        pass

    @classmethod
    def delete(cls, channel):
        """
        Deletes the Channel model entry in the database that matches the channel_id provided
        :param channel: An instance of Channel
        :return: None
        """
        pass