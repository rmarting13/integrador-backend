from app.database import DatabaseConnection as db


class User:
    """
    A class which represents a User data model
    """
    def __init__(self, **kwargs):
        """
        :keyword user_id: (``int``)
        :keyword status_id: (``int``)
        :keyword username: (``str``)
        :keyword password: (``str``)
        :keyword first_name: (``str``)
        :keyword last_name: (``str``)
        :keyword email: (``str``)
        :keyword phone_number: (``str``)
        :keyword creation_date: (``datetime``)
        :keyword last_login: (``datetime``)
        :keyword profile_picture: (``str``)
        """
        self.user_id = kwargs.get('user_id', None)
        self.status_id = kwargs.get('status_id', None)
        self.username = kwargs.get('username', None)
        self.password = kwargs.get('password', None)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.email = kwargs.get('email', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.creation_date = kwargs.get('creation_date', None)
        self.last_login = kwargs.get('last_login', None)
        self.profile_picture = kwargs.get('last_login', None)

    def __str__(self):
        """
        :return : A string representation of the User data object
        """
        return f"""
                user_id: {self.user_id}
                status_id: {self.status_id}
                username: {self.username}
                password: {self.password}
                first_name: {self.first_name}
                last_name: {self.last_name}
                email: {self.email}
                phone_number: {self.phone_number}
                creation_date: {self.creation_date}
                last_login: {self.last_login}
                """

    @classmethod
    def get(cls, user):
        """
        Gets the User model entry in database that matches the user_id provided
        :param user: An instance of User with a not null user_id
        :return: User or None
        """
        query = "SELECT * FROM users WHERE user_id = %s;"
        params = user.user_id,
        result = db.fetch_one(query=query, params=params)
        if result:
            attrs = vars(user).keys()
            items = list(zip(attrs, result))
            kwargs = {}
            for key, value in items:
                kwargs.update({key: value})
            return cls(**kwargs)
        else:
            return None

    @classmethod
    def get_all(cls):
        """
        Gets a collection of all User entries existing in the database
        :return: A User list or None
        """
        query = "SELECT * FROM users;"
        result = db.fetch_all(query=query)
        if result:
            attrs = vars(User()).keys()
            users = []
            for row in result:
                kwargs = {}
                for key, value in zip(attrs, row):
                    kwargs.update({key: value})
                users.append(cls(**kwargs))
            return users
        else:
            return None

    @classmethod
    def get_by_username(cls, user):
        """
        Gets all User entries from the database that matches the provided username
        :param user: An instance of User with a not null username
        :return: A User list or None
        """
        query = "SELECT * FROM users WHERE username LIKE %s ORDER BY username;"
        params = '%' + user.username + '%',
        result = db.fetch_all(query=query, params=params)
        if result:
            attrs = vars(User()).keys()
            users = []
            for row in result:
                kwargs = {}
                for key, value in zip(attrs, row):
                    kwargs.update({key: value})
                users.append(cls(**kwargs))
            return users
        else:
            return None

    @classmethod
    def create(cls, user):
        """
        Creates a new User model entry in the database
        :param user: An instance of User
        :return: None
        """
        query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s);"
        params = user.username, user.password, user.email
        db.execute_query(query=query, params=params)

    @classmethod
    def update(cls, user):
        """
        Updates the values of the User model entry in the database that matches the user_id provided
        :param user: An instance of User
        :return: None
        """
        allowed_columns = {'status_id', 'username', 'password',
                           'first_name', 'last_name', 'email',
                           'phone_number', 'profile_picture'}
        query_parts = []
        params = []
        for key, value in vars(user).items():
            if key in allowed_columns and value:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(user.user_id)
        query = "UPDATE users SET " + ", ".join(query_parts) + " WHERE user_id = %s;"
        db.execute_query(query, params=params)

    @classmethod
    def delete(cls, user):
        """
        Deletes the User model entry in the database that matches the user_id provided
        :param user: An instance of User
        :return: None
        """
        query = "DELETE FROM users WHERE user_id = %s;"
        params = user.user_id,
        db.execute_query(query=query, params=params)


if __name__ == '__main__':

    obj = User(
        user_id=1,
    )

    # User.update(obj)
    # user = User.get(obj)
    # print(user)
    # User.delete(obj)

    user = User.get(obj)
    print(type(user.creation_date))
    #print(*users, sep='\n')