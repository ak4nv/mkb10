import os
import logging

from logging.handlers import SMTPHandler
from importlib import import_module

from flask import jsonify, request, render_template

XHR_HDRS = (("Access-Control-Allow-Credentials", "true"),
            ("Access-Control-Allow-Methods", "GET,POST"))


def add_xhr_headers(resp):
    resp.headers.extend(XHR_HDRS)
    if request.blueprint == "api":
        # Enable CORS for `api` blueprint
        resp.headers.add("Access-Control-Allow-Origin",
                         request.headers.get("Origin", "*"))


def handle_error(e):
    err_name = getattr(e, "name", "Internal Server Error")
    err_code = getattr(e, "code", 500)
    return jsonify(err=err_name), err_code


def register_blueprints(app):
    app_dir = os.path.join(app.root_path, app.import_name)
    listdir = (name for name in os.listdir(app_dir)
               if os.path.isdir(os.path.join(app_dir, name)))
    for d in listdir:
        try:
            m = import_module(".".join((app.import_name, d)))
        except (ImportError, TypeError) as e:
            if app.debug:
                raise e
        if hasattr(m, "bp"):
            # app.logger.debug(f"Registered blueprint `{d}`")
            app.register_blueprint(m.bp, **getattr(m, "options", {}))


def enable_sql_dump(app):
    # Enable dump sql query into console
    logger = logging.getLogger("peewee")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
