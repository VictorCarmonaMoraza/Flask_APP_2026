from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField


class RegisterFormWtf(FlaskForm):
    username = StringField('Nombre de usuario:')
    password = PasswordField('Contraseña:')
    submit = SubmitField('Registrar')