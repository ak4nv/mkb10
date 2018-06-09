from flask import Flask, Response, abort, jsonify, request

import os

from config import db
from app.utils import (add_xhr_headers, handle_error, register_blueprints,
                       CustomJSONEncoder)


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object('config.default')
    app.config.from_pyfile('../settings.py', silent=True)
    app.name = app.config.get('APP_NAME', 'app')

    db.init_app(app)
    @db.database.func('lower_case')
    def lower_case(value):
        return value.lower()


    register_blueprints(app, 'app')

    app.json_encoder = CustomJSONEncoder

    @app.before_request
    def early_response():
        if request.method == 'OPTIONS':
            # Early response for preflight request
            resp = Response('Test passed')
            add_xhr_headers(resp)
            return resp

    @app.after_request
    def set_access_control_header(resp):
        if request.is_xhr:
            add_xhr_headers(resp)
        return resp

    if app.debug:
        if app.config.get('DEBUG_SQL', False):
            from app.utils import enable_sql_dump
            enable_sql_dump(app)
    else:
        from app.utils import get_mail_handler
        app.logger.addHandler(get_mail_handler(app))

    for e in (401, 403, 404, 500):
        app.errorhandler(e)(handle_error)

    @app.url_defaults
    def versioning_static_files(endpoint, values):
        filename = values.get('filename')
        if endpoint == 'static' and filename:
            fp = os.path.join(app.static_folder, filename)
            if os.path.exists(fp):
                values['_'] = int(os.stat(fp).st_mtime)

    return app
