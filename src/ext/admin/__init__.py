from flask import Flask
from flask_admin import Admin

admin = Admin()


def init_app(app: Flask) -> None:
    admin.init_app(app)
