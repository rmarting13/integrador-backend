from flask import Blueprint
from app.models.exceptions import Forbidden

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(Forbidden)
def handle_forbidden(error):
	return error.get_response()

