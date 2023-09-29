from io import BytesIO

from flask import request, session, send_file
from flask_cors import cross_origin
import base64
from ..models.user import User
from ..models.exceptions import Forbidden, ServerError, BadRequest, NotFound



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
        user_id = session.get('user_id')
        user = User.get(User(user_id=user_id))
        if user:
            return vars(user), 200
        else:
            return NotFound

    @classmethod
    def download_file(cls):
        user_id = session['user_id']
        user = User.get_picture(User(user_id=user_id))
        if user:
            return send_file(BytesIO(user.profile_picture), mimetype='image/png'), 200

    @classmethod
    def current_password(cls, pw):
        user = User.get(User(user_id=session.get('user_id')))
        if user.password == pw:
            return {'message': 'Current password matches correctly'}, 200
        return {'error': 'Invalid current password'}, 400

    @classmethod
    def upload_file(cls):
        file = request.files['file'].read()
        user_id = session['user_id']
        user = User(user_id=user_id, profile_picture=file)
        User.update(user)
        return {}, 200

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
        return NotFound

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
        return NotFound

    @classmethod
    def create(cls):
        """
        Creates a new user resource
        :return: A Flask Response object
        """
        data = request.json
        print(data)
        user = User(**data)
        if not User.already_exists(user):
            session['user_id'] = User.create(user)
            session['username'] = data.get('username')
            return {'message': 'User created successfully'}, 201
        return {'error': 'Username and email already exists'}, 400

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
