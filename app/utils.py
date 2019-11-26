from flask import current_app, jsonify, request, render_template

import os
import logging
from logging.handlers import SMTPHandler

from importlib import import_module
from datetime import date, time, datetime

XHR_HDRS = (('Access-Control-Allow-Credentials', 'true'),
            ('Access-Control-Allow-Methods', 'GET,POST'),
            ('Access-Control-Allow-Headers', 'Content-Type,X-Requested-With'))


def add_xhr_headers(resp):
    resp.headers.extend(XHR_HDRS)
    if request.blueprint == 'api':
        # Enable CORS for `api` blueprint
        resp.headers.add('Access-Control-Allow-Origin',
                         request.headers.get('Origin', '*'))


def handle_error(e):
    err_name = getattr(e, 'name', 'Internal Server Error')
    err_code = getattr(e, 'code', 500)

    if request.is_xhr:
        return jsonify(err=err_name), err_code

    return render_template('%s.html' % err_code, name=err_name), err_code


def register_blueprints(app):
    app_dir = os.path.join(app.root_path, app.import_name)
    listdir = (name for name in os.listdir(app_dir)
               if os.path.isdir(os.path.join(app_dir, name)))
    for d in listdir:
        try:
            m = import_module('.'.join((app.import_name, d)))
        except (ImportError, TypeError) as e:
            if app.debug:
                raise e
        if hasattr(m, 'bp'):
            # app.logger.debug(f'Registered blueprint `{d}`')
            app.register_blueprint(m.bp, **getattr(m, 'options', {}))


def get_mail_handler(app):
    # Settings handler for email about exceptions
    mailhost = (app.config.get('MAIL_SERVER', 'localhost'),
                app.config.get('MAIL_PORT', 1025))
    fromaddr = app.config.get('MAIL_DEFAULT_SENDER',
                              '{} <{}>'.format(app.name,
                                               app.config['ADMINS'][0]))
    toaddrs = app.config['ADMINS']
    subject = '{} app error'.format(app.name)
    credentials = (app.config.get('MAIL_USERNAME'),
                   app.config.get('MAIL_PASSWORD'))
    secure = app.config.get('MAIL_USE_TLS')
    handler = SMTPHandler(mailhost, fromaddr, toaddrs,
                          subject, credentials, secure)

    handler.setLevel(logging.ERROR)
    return handler


def enable_sql_dump(app):
    # Enable dump sql query into console
    logger = logging.getLogger('peewee')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
