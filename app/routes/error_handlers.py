from flask import Blueprint
from app.models.exceptions import Forbidden, ServerError, BadRequest, NotFound

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Forbidden)
def handle_forbidden(error):
    return error.get_response()


@errors.app_errorhandler(ServerError)
def handle_server_error(error):
    return error.get_response()

@errors.app_errorhandler(BadRequest)
def handle_BadRequest(error):
    return error.get_response()

@errors.app_errorhandler(NotFound)
def handle_NotFound(error):
    return error.get_response()


