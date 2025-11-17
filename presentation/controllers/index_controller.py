from flask import Blueprint, render_template, url_for

from application.use_cases.index_use_case import IndexUseCase
from datetime import datetime

from utils.repeat_utils import repeat

index_bp = Blueprint('index', __name__)


@index_bp.route('/', methods=['GET'])
def index():
    message = IndexUseCase().execute()
    return message


@index_bp.route('/index/<name>/<int:age>', methods=['GET'])
@index_bp.route('/index/<name>', methods=['GET'])
@index_bp.route('/index', methods=['GET'])
def index2(name=None, age=None):
    message = IndexUseCase().execute2(name=name, age=age)
    return message


@index_bp.route('/index_plantilla', methods=['GET'])
def index_plantilla():
    print(url_for('index.index'))
    print(url_for('index.index',name='Victor'))
    print(url_for('index.index',name='Victor',age=35))
    name = 'Victor'
    return render_template('index.html', name=name)


@index_bp.route('/index_plantilla_lista', methods=['GET'])
def index_plantilla_lista():
    lista = IndexUseCase().obtener_lista()
    return render_template('index_lista.html', lista=lista)


@index_bp.route('/index_plantilla_lista_filtro', methods=['GET'])
def index_plantilla_lista_filtro():
    lista = IndexUseCase().obtener_lista()
    date = datetime.now()
    return render_template('index_plantilla_filtro.html', lista=lista, date=date, repeat=repeat)


@index_bp.route('/index_dict/<name>/<int:age>/<email>', methods=['GET'])
@index_bp.route('/index_dict/<name>/<int:age>', methods=['GET'])
@index_bp.route('/index_dict/<name>', methods=['GET'])
@index_bp.route('/index_dict', methods=['GET'])
def index_diccionario(name=None, age=None, email=None):
    diccionario = IndexUseCase().obtener_diccionario(name=name, age=age, email=email)
    return render_template('index_plantilla_diccionario.html', data=diccionario)
