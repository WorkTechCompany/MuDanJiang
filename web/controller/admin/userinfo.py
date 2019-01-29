from web.controller.admin import route_admin
from common.libs.WebHelper import ops_render
from common.model.user import user
from application import db
from flask import request, jsonify


@route_admin.route('/userinfo/', methods=['GET', 'POST'])
def userinfo():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}
    req = request.values
    page = req['page'] if 'page' in req else 1
    offset = int(int(page) - 1) * 100

    query = user.query

    totalCount = query.count()
    list = query.offset(offset).limit(100).all()

    resp['totalCount'] = totalCount
    resp['list'] = list
    resp['pageTotal'] = (totalCount // 100) + 1
    resp['curPage'] = page
    resp['type'] = type

    return ops_render('/admin/user.html', resp)

