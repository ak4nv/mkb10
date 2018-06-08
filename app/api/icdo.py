from flask import jsonify, request
from app.models import MKBO


def get_icdo_blocks():
    qs = (MKBO
          .select(MKBO.id, MKBO.name)
          .where(MKBO.id_parent >> None))
    return jsonify(tuple(qs.dicts()))


def get_icdo_block(id):
    qs = (MKBO
          .select(MKBO.code, MKBO.name)
          .where(MKBO.id_parent == id))
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
          .where(MKB10.id_parent.is_null(False)))

    if q.isdigit():
        qs = qs.where(MKB10.code.startswith(q))
    else:
        qs = qs.where(MKB10.name.contains(q))

    limit = request.args.get('limit', '50')
    qs = qs.limit(int(limit) if limit.isdigit() else 50)

    return jsonify(tuple(qs.dicts()))
