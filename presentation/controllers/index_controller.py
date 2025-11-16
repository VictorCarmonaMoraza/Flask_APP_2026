from flask import Blueprint

from application.use_cases.index_use_case import IndexUseCase

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    message = IndexUseCase().execute()
    return message
