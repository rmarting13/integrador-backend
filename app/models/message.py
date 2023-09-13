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
        query = "SELECT * FROM messages WHERE message_id = %s;"
        params = message.message_id,
        result = db.fetch_one(query=query, params=params)
        if result:
            return cls(*result)
        else:
            return None

    @classmethod
    def get_all(cls, message):
        """
        Gets a collection of all Message entries existing in the database
        :return: A Message list or None
        """
        if message:
            query_parts = []
            params = []
            for key, value in vars(message).items():
                if value:
                    query_parts.append(key)
                    params.append('%'+value+'%')
            if len(query_parts) > 1:
                query = f"SELECT * FROM messages WHERE {query_parts.pop(0)}"+' LIKE %s AND '.join(query_parts) + ";"
            else:
                query = f"SELECT * FROM messages WHERE {query_parts.pop()} LIKE %s;"
            result = db.fetch_all(query=query, params=params)
        else:
            query = "SELECT * FROM messages"
            result = db.fetch_all(query=query)
        if result:
            messages = []
            for row in result:
                messages.append(cls(*row))
            return messages
        else:
            return None

    @classmethod
    def create(cls, message):
        """
        Creates a new Message model entry in the database
        :param message: An instance of Message
        :return: None
        """
        query = "INSERT INTO messages (user_id, channel_id, content, edited) VALUES (%s, %s, %s, %s);"
        params = message.user_id, message.channel_id, message.content, message.edited
        db.execute_query(query=query, params=params)

    @classmethod
    def update(cls, message):
        """
        Updates the values of the Message model entry in the database that matches the message_id provided
        :param message: An instance of Message
        :return: None
        """
        query = "UPDATE messages SET content = %s, edited = True WHERE message_id = %s;"
        params = message.content, message.message_id
        db.execute_query(query, params=params)

    @classmethod
    def delete(cls, message):
        """
        Deletes the Message model entry in the database that matches the message_id provided
        :param message: An instance of Message
        :return: None
        """
        query = "DELETE FROM messages WHERE message_id = %s;"
        params = message.message_id,
        db.execute_query(query=query, params=params)

if __name__ == '__main__':

    msg = Message(
        message_id=2,
        user_id=1,
        content='the fourth message'
    )
    args = {'user_id': 1, 'content': 'testing message'}
    msg2 = Message(**args)
    
    print(msg2)
    # Message.create(msg)
    # Message.update(msg)
    # messages = Message.get_by_content(msg)
    # print(message)
    # Message.delete(msg)
    # messages = Message.get_all()
    # print(*messages, sep='\n')
