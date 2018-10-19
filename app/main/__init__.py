from flask import Blueprint, render_template, redirect, request

bp = Blueprint('main', __name__)


@bp.route('/')
def main_page():
    return render_template('index.html',
                           BASE_URL=request.script_root.lstrip('/'))


@bp.route('/<path:path>')
def redir(path):
    return redirect('/#/{}'.format(path))
