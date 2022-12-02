from flask import Flask

from .auth import views as AuthView


def load_app_blueprints(app: Flask) -> None:
    app.register_blueprint(AuthView.blueprint)
