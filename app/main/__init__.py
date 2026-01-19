from flask import Blueprint, render_template

bp = Blueprint("main", __name__, template_folder="templates")


@bp.route("/")
def main_page():
    return render_template("base.jinja")


@bp.route("/readme")
def readme_page():
    with open("README.md") as f:
        readme = f.read()
    return render_template("index.jinja", readme=readme)


@bp.route("/mkb-tree")
def mkb_tree_page():
    return render_template("mkb_tree.jinja")


@bp.route("/mkb")
def mkb_page():
    return render_template("mkb.jinja")


@bp.route("/mkbo-tree")
def mkbo_tree_page():
    return render_template("mkbo_tree.jinja")

@bp.route("/mkbo")
def mkbo_page():
    return render_template("mkbo.jinja")
