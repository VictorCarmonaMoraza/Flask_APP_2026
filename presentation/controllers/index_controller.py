from flask import Blueprint

from application.use_cases.index_use_case import IndexUseCase

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    message = IndexUseCase().execute()
    return message

@index_bp.route('/index/<name>/<int:age>', methods=['GET'])
@index_bp.route('/index/<name>', methods=['GET'])
@index_bp.route('/index', methods=['GET'])
def index2(name=None,age=None):
    message = IndexUseCase().execute2(name=name,age=age)
    return message
