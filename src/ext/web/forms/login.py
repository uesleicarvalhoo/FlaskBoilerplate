from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    username = StringField("Usuario", [Required("Informe o usuário")])
    password = PasswordField("Usuario", [Required("Informe o usuário")])
