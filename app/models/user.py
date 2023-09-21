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
        self.profile_picture = kwargs.get('profile_picture', None)

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
    def is_registered(cls, user):
        query = "SELECT user_id FROM users WHERE username = %s AND password = %s;"
        params = (user.username, user.password)
        result = db.fetch_one(query, params=params)
        if result:
            return result[0]
        return False

    @classmethod
    def already_exists(cls, user):
        query = "SELECT username, email FROM users WHERE username = %s AND email = %s;"
        params = (user.username, user.email)
        result = db.fetch_one(query=query, params=params)
        if result:
            return True
        return False

    @classmethod
    def get(cls, user):
        """
        Gets the User model entry in database that matches the user_id provided
        :param user: An instance of User with a not null user_id
        :return: User or None
        """
        attrs = vars(user).keys()
        query = f"SELECT {', '.join(attrs)} FROM users WHERE user_id = %s;"
        params = user.user_id,
        result = db.fetch_one(query=query, params=params)
        if result:
            items = list(zip(attrs, result))
            kwargs = {}
            for key, value in items:
                kwargs.update({key: value})
            return cls(**kwargs)
        else:
            return None

    @classmethod
    def get_all(cls, user=None):
        """
        Gets a collection of all User entries existing in the database or
        those that matches user's data provided by param
        :return: A User list or None
        """
        attrs = vars(User()).keys()
        if user:
            query_parts = []
            params = []
            for key, value in vars(user).items():
                if value:
                    query_parts.append(key)
                    params.append('%'+value+'%')
            if len(query_parts) > 1:
                query = (f"SELECT {', '.join(attrs)} FROM users WHERE {query_parts.pop(0)}" +
                         ' LIKE %s AND '.join(query_parts) + ";")
            else:
                query = f"SELECT {', '.join(attrs)} FROM users WHERE {query_parts.pop()} LIKE %s;"
            result = db.fetch_all(query=query, params=params)
        else:
            query = f"SELECT {', '.join(attrs)} FROM users;"
            result = db.fetch_all(query=query)
        if result:
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

    obj1 = User(
        status_id=1,
        username='obito',
        password='1234',
        email='obichiha@outlook.com',
        phone_number='3216541',
    )
    obj2 = User(
        status_id=1,
        username='rasen86',
        password='1234',
        email='naruzumaki@gmail.com',
        phone_number='3216541',
    )
    obj3 = User(
        status_id=0,
        username='sasuke_kun21',
        password='1234',
        email='sasukeuchiha@gmail.com',
        phone_number='3216541',
    )
    obj4 = User(
        status_id=1,
        username='sakurachan',
        password='1234',
        email='sakura_21@outlook.com',
        phone_number='3216541',
    )
    obj5 = User(
        status_id=0,
        username='madarachiha',
        password='1234',
        email='madara_uchiha@outlook.com',
        phone_number='3216541',
    )
    obj6 = User(
        status_id=0,
        username='kakashi21',
        password='1234',
        email='kakashisensei@gmail.com',
        phone_number='3216541',
    )
    obj7 = User(
        status_id=0,
        username='orochi21',
        password='1234',
        email='orochimaru_senin@gmail.com',
        phone_number='3216541',
    )
    obj8 = User(
        status_id=1,
        username='erosenin',
        password='1234',
        email='jiraija@outlook.com',
        phone_number='3216541',
    )
    obj9 = User(
        status_id=1,
        username='innoyam',
        password='1234',
        email='inno_yamanaka@outlook.com',
        phone_number='3216541',
    )
    # to_create = [obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9]
    # for obj in to_create:
    #     User.create(obj)

    # print(vars(obj))
    # User.update(obj)
    # user = User.get(obj)
    # print(user)
    # User.delete(obj)

    # user = User.get(obj)
    # print(type(user.creation_date))
    result = User.get_all(User(username='martin'))
    print(result[0])
    # users = User.get_all(user)
    # if users:
    #     print(*users, sep=''.center(50, '-'))
