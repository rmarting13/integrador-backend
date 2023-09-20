from flask import request, session
from flask_cors import cross_origin

from ..models.user import User


class UserController:
    """User controller class that binds user resource requests to user data model."""

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            username=data.get('username'),
            password=data.get('password')
        )
        id = User.is_registered(user)
        if id:
            session['username'] = data.get('username')
            session['user_id'] = id
            # session['SameSite'] = True
            return {"message": "Successfully logged in"}, 200
        return {"error": "Wrong username or password"}, 401

    @classmethod
    def logout(cls):
        session.pop('username', None)
        session.pop('user_id', None)
        return {"message": "Successfully logged out"}, 200

    @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get_all(User(username=username))
        if user:
            return vars(user.pop(0)), 200
        else:
            return {"error": "User data not found"}, 404

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
    def update(cls):
        """
        Updates a user resource by id
        :return: A Flask Response object
        """
        data = request.json
        data['user_id'] = session.get('user_id')
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
