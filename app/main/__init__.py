from flask import Blueprint, render_template, redirect

bp = Blueprint('main', __name__)


@bp.route('/')
def main_page():
    return render_template('index.html')


@bp.route('/<path:path>')
def redir(path):
    return redirect('/')
