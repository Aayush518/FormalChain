from flask import Blueprint

blockchain_bp = Blueprint('blockchain', __name__, url_prefix='/blockchain')
user_bp = Blueprint('user', __name__, url_prefix='/user')

from . import routes
