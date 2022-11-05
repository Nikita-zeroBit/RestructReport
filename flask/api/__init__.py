import os
from flask import Flask, send_from_directory
from flask_uuid import FlaskUUID

from .blueprints import load_app_blueprints
from .commands import load_commands
from .config import load_app_config
from .database import init_database


def create_app() -> Flask:

    app = Flask(__name__, static_folder='../static', template_folder='../templates')

    @app.route('/static/<path:path>')
    def send_report(path):
        return send_from_directory('../static', path)

    flask_uuid = FlaskUUID()
    flask_uuid.init_app(app)

    load_app_config(app)
    init_database(app)
    load_app_blueprints(app)
    load_commands(app)

    return app
