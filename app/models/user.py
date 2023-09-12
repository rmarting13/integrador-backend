from app.database import DatabaseConnection as db


class User:
    """
    A class which represents a user's data model
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
        pass

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_by_username(cls, user):
        pass

    @classmethod
    def create(cls, user):
        pass

    @classmethod
    def update(cls, user):
        pass

    @classmethod
    def delete(cls, user):
        pass


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