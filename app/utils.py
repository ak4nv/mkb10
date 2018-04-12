from flask import current_app, jsonify, request, render_template
from flask.json import JSONEncoder

import os
import logging
from logging.handlers import SMTPHandler

from importlib import import_module
from datetime import date, time, datetime


def handle_error(e):
    err_name = getattr(e, 'name', 'Internal Server Error')
    err_code = getattr(e, 'code', 500)

    if request.is_xhr:
        return jsonify(err=err_name), err_code

    return render_template('%s.html' % err_code, name=err_name), err_code


def register_blueprints(app, bps_dir):
    app_dir = os.path.join(os.getcwd(), bps_dir)
    listdir = (name for name in os.listdir(app_dir)
               if os.path.isdir(os.path.join(app_dir, name)))
    for d in listdir:
        try:
            m = import_module('.'.join((bps_dir, d)))
        except (ImportError, TypeError) as e:
            app.logger.exception(e)
            continue
        if hasattr(m, 'bp'):
            # app.logger.debug('Registered blueprint `{}`'.format(d))
            app.register_blueprint(m.bp, **getattr(m, 'options', {}))


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M')
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, time):
            return obj.strftime('%H:%M')
        return super().default(obj)


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
