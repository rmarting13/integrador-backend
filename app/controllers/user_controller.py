from ..models.exceptions import FilmNotFound, InvalidDataError
from ..models.film_model import Film

from flask import request

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
        pass

    @classmethod
    def get_all(cls):
        """
        Gets all users resources
        :return: A Flask Response object
        """
        pass

    @classmethod
    def create(cls):
        """
        Creates a new user resource
        :return: A Flask Response object
        """
        pass

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
