import os

from flask import Flask, request

from app import utils
from app.models import db


def create_app(config):
    app = Flask("app", root_path=os.getcwd())
    app.config.from_pyfile(config)

    db.init_app(app)
    utils.register_blueprints(app)

    @app.before_request
    def early_response():
        if request.method == "OPTIONS":
            # Early response for preflight request
            return app.make_response("CORS has been allowed")

    @app.after_request
    def set_access_control_header(resp):
        if request.method == "OPTIONS":
            utils.add_xhr_headers(resp)
        return resp

    if app.debug:
        if app.config.get("DEBUG_SQL", False):
            utils.enable_sql_dump(app)

    for e in (404, 500):
        app.errorhandler(e)(utils.handle_error)

    return app
