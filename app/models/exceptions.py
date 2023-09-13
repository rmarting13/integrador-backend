from werkzeug.exceptions import HTTPException
from flask import jsonify


class Forbiden(HTTPException):
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

