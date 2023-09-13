from flask import request
from ..models.user import User


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
        return {'error': 'Source not found'}, 404

    @classmethod
    def get_all(cls):
        """
        Gets all users resources
        :return: A Flask Response object
        """
        data = request.args
        user = None
        if data:
            result = User.get_all(User(**data))
        else:
            result = User.get_all()
        if result:
            return list(map(lambda u: vars(u), result)), 200
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
        data = request.json
        data['user_id'] = user_id
        user = User(**data)
        User.update(user)
        return {'message': 'User updated successfully'}, 200

    @classmethod
    def delete(cls, user_id):
        """
        Deletes a user resource by id
        :param user_id: (´´int´´)
        :return: A Flask Response object
        """
        user = User(user_id=user_id)
        User.delete(user)
        return {}, 204
