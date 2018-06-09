from flask import jsonify, request
from app.models import MKBO


def get_icdo_blocks():
    qs = (MKBO
          .select(MKBO.id, MKBO.name)
          .where(MKBO.parent >> None))
    return jsonify(tuple(qs.dicts()))


def get_icdo_block(id):
    qs = (MKBO
          .select(MKBO.code, MKBO.name)
          .where(MKBO.parent == id))
    return jsonify(tuple(qs.dicts()))


def fetch_icdo():
    codes = list(filter(bool, request.args.get('codes', '').split(','))) \
        or request.get_json()
    if not codes:
        return jsonify(err='bad_param', msg='missing required parameter: codes')
    qs = (MKBO
          .select(MKBO.code, MKBO.name)
          .where(MKBO.code << codes))
    return jsonify(tuple(qs.dicts()))


def lookup_icdo():
    q = request.args.get('q')
    if not q:
        return jsonify(err='bad_param', msg='missing required parameter: q')
    qs = (MKBO
          .select(MKBO.code, MKBO.name)
          .where(MKBO.parent.is_null(False)))

    if q.isdigit():
        qs = qs.where(MKBO.code.startswith(q))
    else:
        qs = qs.where(MKBO.name_lower.contains(q.lower()))

    limit = request.args.get('limit', '50')
    qs = qs.limit(int(limit) if limit.isdigit() else 50)

    return jsonify(tuple(qs.dicts()))
