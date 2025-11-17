from flask import Blueprint, render_template, request

from domain.models.register import RegisterFormWtf

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


@auth_bp.route('/auth/registerWTF', methods=['GET','POST'])
def authWTF():
    form_wtf = RegisterFormWtf()
    if form_wtf.validate_on_submit():
        name = form_wtf.username.data
        password = form_wtf.password.data
        print(f'{name} - {password}')
    return render_template('auth/register_wtf.html',form=form_wtf)