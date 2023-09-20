from werkzeug.exceptions import HTTPException
from flask import jsonify
from werkzeug.sansio.response import Response


class Forbidden(HTTPException):
    def __init__(self, description = "Not allowed for this user"):
        super().__init__(description)
        self.status_code = 403

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class ServerError(HTTPException):
    def __init__(self, description="Server is not responding"):
        super().__init__(description)
        self.status_code = 500

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class BadRequest(HTTPException):
    def __init__(self, description="Bad request"):
        super().__init__(description)
        self.status_code = 400
    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class NotFound(HTTPException):
    def __init__(self, description="Source not found"):
        super().__init__(description)
        self.status_code = 404
    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

