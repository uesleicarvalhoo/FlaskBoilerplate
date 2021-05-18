from flask import Flask

from src.ext import admin, api, auth, config, database, web


def create_app() -> Flask:
    app = Flask(__name__)

    config.init_app(app)
    auth.init_app(app)
    database.init_app(app)
    admin.init_app(app)
    api.init_app(app)
    web.init_app(app)

    return app
