from flask import Flask

from src.settings import SECRET_KEY, SQLALCHEMY_DB_URI


def init_app(app: Flask) -> None:
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DB_URI
