from flask import Blueprint, render_template, redirect, request

bp = Blueprint('main', __name__)


@bp.route('/')
def main_page():
    prefix = ''
    if request.script_root:
        prefix = request.script_root.lstrip('/') + '/'
    return render_template('index.html', BASE_URL=prefix)


@bp.route('/<path:path>')
def redir(path):
    return redirect('/#/{}'.format(path))
