from web.controller.admin import route_admin
from common.libs.WebHelper import ops_render
from common.model.user import user
from common.model.data import data
from common.model.message import message
from application import db
from flask import request, jsonify


@route_admin.route('/count', methods=['GET', 'POST'])
def count():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}

    query = user.query
    totalCount = query.count()
    resp['usercount'] = totalCount

    query = data.query
    totalCount = query.count()
    resp['datacount'] = totalCount

    query = message.query
    totalCount = query.count()
    resp['messagecount'] = totalCount


    return ops_render('/admin/count.html', resp)
