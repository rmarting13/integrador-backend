from flask import request

from ..models.user import User

from decimal import Decimal


class UserController:
    """User controller class that binds user resource requests to user data model."""

    @classmethod
    def get(cls, user_id):
        """
        Gets a user by id
        :param user_id: (´´int´´)
        :return: A Flask Response object
        """
        user = User(user_id=user_id)
        result = User.get(user)
        if result:
            return vars(result), 200
        else:
            return {'error': 'Source not found'}, 404
        pass

    @classmethod
    def get_all(cls):
        """
        Gets all users resources
        :return: A Flask Response object
        """
        result = User.get_all()
        if result:
            users = []
            for row in result:
                users.append(vars(row))
            return users, 200
        else:
            return {'error': 'Source not found'}, 404

    @classmethod
    def create(cls):
        """
        Creates a new user resource
        :return: A Flask Response object
        """
        data = request.json
        User.create(User(**data))
        return {'message': 'User created successfully'}, 201

    @classmethod
    def update(cls, user_id):
        """
        Updates a user resource by id
        :param user_id: (´´int´´)
        :return: A Flask Response object
        """
        pass

    @classmethod
    def delete(cls, user_id):
        """
        Deletes a user resource by id
        :param user_id: (´´int´´)
        :return: A Flask Response object
        """
        pass
