from typing import Tuple

from flask import Flask
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import check_password_hash

from src.ext.database.models import User
from src.utils.exceptions import DataNotFoundError

auth = LoginManager()


def init_app(app: Flask) -> None:
    auth.init_app(app)


@auth.user_loader
def validate_user(username: str, passwd: str) -> Tuple[bool, str]:
    try:
        user = User.get(username=username)

    except DataNotFoundError:
        return False, 'Usuario "%(username)s" não cadastrado!' % {"username": username}

    else:
        if not check_password_hash(user.password, passwd):
            return False, "Senha invalida!"

        login_user(user)
        return bool, "Usuario logado com sucesso!"


def logout_current_user():
    logout_user()
