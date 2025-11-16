from flask import Blueprint, jsonify

from application.use_cases.say_hello_use_case import SayHelloUseCase

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/', methods=['GET'])
def hello():
    message = SayHelloUseCase().execute()
    return jsonify({"message": message})
