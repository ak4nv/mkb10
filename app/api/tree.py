from peewee import fn, JOIN
from flask import jsonify, request
from app.models import MKB10


def get_classes():
    qs = (MKB10
          .select(MKB10.id, MKB10.name)
          .where(MKB10.parent >> None)
          .where(MKB10.code >> None))
    return jsonify(tuple(qs.dicts()))


def get_blocks(cls):
    qs = (MKB10
          .select(MKB10.id, MKB10.name)
          .where(MKB10.code >> None)
          .where(MKB10.parent == cls))
    return jsonify(tuple(qs.dicts()))


def get_group(block):
    Alias = MKB10.alias()
    qs = (MKB10
          .select(MKB10.code, MKB10.name,
                  (fn.count(Alias.id) > 0).alias('ct'))
          .join(Alias, JOIN.LEFT_OUTER, on=(Alias.parent == MKB10.id))
          .where(MKB10.parent == block)
          .group_by(Alias.parent)
          .order_by(MKB10.code))
    qs = actual_filter(qs)
    return jsonify([f(x) for x in qs.dicts()])


def get_subgroup(group):
    qs = (MKB10
          .select(MKB10.code, MKB10.name)
          .where(MKB10.code.startswith(group + '.')))
    qs = actual_filter(qs)
    return jsonify(tuple(qs.dicts()))


def actual_filter(qs):
    if not 'all' in request.args:
        qs = qs.where(MKB10.actual == True)
    else:
        qs = qs.select_extend(MKB10.actual)
    return qs


def f(obj):
    obj.update(has_subgroup=bool(obj.pop('ct')))
    return obj
