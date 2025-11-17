from flask import Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['GET','POST'])
def auth():
    print(request.form)
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        print(f'{name} - {password}')
    return render_template('auth/register.html')