from flask import Blueprint, render_template, request

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['GET','POST'])
def auth():
    print(request.form)
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        if len(name)>=4 and len(name)<=6 and len(password)>=6 and len(password)<=40:
            print(f'{name} - {password}')
        else:
            error ="""El nombre de usuario debe tener entre 4 y 25 caractyres y la contraseña entre 6 y 40 caracteres"""
            return render_template('auth/register.html', error=error)
    return render_template('auth/register.html')