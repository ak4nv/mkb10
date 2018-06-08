from flask import Blueprint
from . import tree, find, icdo

bp = Blueprint('api', __name__)
options = {'url_prefix': '/api'}


bp.add_url_rule('', view_func=tree.get_classes)
bp.add_url_rule('/<int:cls>', view_func=tree.get_blocks)
bp.add_url_rule('/<int:block>/group', view_func=tree.get_group)
bp.add_url_rule('/<string:group>/subgroup', view_func=tree.get_subgroup)
bp.add_url_rule('/fetch', view_func=find.fetch_icd, methods=('GET', 'POST'))
bp.add_url_rule('/lookup', view_func=find.lookup_icd)


bp.add_url_rule('/icdo/block', view_func=icdo.get_icdo_blocks)
bp.add_url_rule('/icdo/block/<int:id>', view_func=icdo.get_icdo_block)
bp.add_url_rule('/icdo/lookup', view_func=icdo.lookup_icdo)
bp.add_url_rule('/icdo/fetch', view_func=icdo.fetch_icdo,
                methods=('GET', 'POST'))
