from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['GET'])
def auth():
    return render_template('auth/register.html')