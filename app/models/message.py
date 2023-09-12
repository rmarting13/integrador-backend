from app.database import DatabaseConnection as db


class Message:
    """
    A class which represents a Message data model
    """
    def __init__(self, message_id=None, user_id=None, channel_id=None,
                 content=None, creation_date=None, edited=None):
        """

        :param message_id: (``int``)
        :param user_id: (``int``)
        :param channel_id: (``int``)
        :param content: (``str``)
        :param creation_date: (``datetime``)
        :param edited: (``bool``)
        """
        self.message_id = message_id
        self.user_id = user_id
        self.channel_id = channel_id
        self.content = content
        self.creation_date = creation_date
        self.edited = edited

    def __str__(self):
        """
        :return : A string representation of the Message data object
        """
        return f"""
                message_id: {self.message_id}
                user_id: {self.user_id}
                channel_id: {self.channel_id}
                content: {self.content}
                creation_date: {self.creation_date}
                edited: {self.edited}
                """

    @classmethod
    def get(cls, message):
        """
        Gets the Message model entry in database that matches the message_id provided
        :param message: An instance of Message with a not null message_id
        :return: Message or None
        """
        pass

    @classmethod
    def get_all(cls):
        """
        Gets a collection of all Message objects existing in database
        :return: A Message list or None
        """
        pass

    @classmethod
    def get_by_user_id(cls, message):
        """
        Gets all Message from database that matches the provided user_id
        :param message: An instance of Message with a not null user_id
        :return: A Message list or None
        """
        pass

    @classmethod
    def get_by_channel_id(cls, message):
        """
        Gets all Message from database that matches the provided channel_id
        :param message: An instance of Message with a not null channel_id
        :return: A Message list or None
        """
        pass

    @classmethod
    def create(cls, message):
        """
        Creates a new Message model entry in the database
        :param message: An instance of Message
        :return: None
        """
        pass

    @classmethod
    def update(cls, message):
        """
        Updates the values of the Message model entry in the database that matches the message_id provided
        :param message: An instance of Channel
        :return: None
        """
        pass

    @classmethod
    def delete(cls, message):
        """
        Deletes the Message model entry in the database that matches the message_id provided
        :param message: An instance of Message
        :return: None
        """
        pass