import re
from peewee import fn
from flask import jsonify, request
from app.models import MKB10


def fetch_icd():
    codes = list(filter(bool, request.args.get('codes', '').split(','))) \
        or request.get_json()
    if not codes:
        return jsonify(err='bad_param', msg='missing required parameter: codes')
    qs = (MKB10
          .select(MKB10.code, MKB10.name)
          .where(MKB10.code << codes))
    return jsonify(tuple(qs.dicts()))


def lookup_icd():
    q = request.args.get('q')
    if not q:
        return jsonify(err='bad_param', msg='missing required parameter: q')
    qs = (MKB10.select(MKB10.name, MKB10.code)
          .where(MKB10.actual == True)
          .where(MKB10.code.is_null(False)))

    if re.match('[a-z]', q[0], re.IGNORECASE):
        qs = qs.where(MKB10.code.startswith(q))
    else:
        qs = qs.where(fn.lower_case(MKB10.name).contains(q.lower()))

    limit = request.args.get('limit', '50')
    qs = qs.limit(int(limit) if limit.isdigit() else 50)

    return jsonify(tuple(qs.dicts()))
