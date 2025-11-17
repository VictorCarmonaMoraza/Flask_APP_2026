from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class RegisterFormWtf(FlaskForm):
    username = StringField('Nombre de usuario:',validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Contraseña:', validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Registrar')