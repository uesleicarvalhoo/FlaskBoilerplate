from flask import Flask

from src.ext.web.routers import main


def init_app(app: Flask) -> None:
    app.register_blueprint(main.bp)
