from web.controller.admin import route_admin
from common.libs.WebHelper import ops_render
from common.model.admin import Admin
from application import db
from flask import request, jsonify




@route_admin.route('/conrtol/', methods=['GET', 'POST'])
def conrtol():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}
    req = request.values
    page = req['page'] if 'page' in req else 1
    power = req['power'] if 'power' in req else -1
    offset = int(int(page) - 1) * 100

    query = Admin.query

    if power != -1:
        query = Admin.query.filter_by(power=power)

    totalCount = query.count()
    list = query.offset(offset).limit(100).all()

    resp['totalCount'] = totalCount
    resp['list'] = list
    resp['pageTotal'] = (totalCount // 100) + 1
    resp['curPage'] = page
    resp['type'] = type

    return ops_render('/admin/admin.html', resp)


@route_admin.route('/deleteconrtol/', methods=['GET', 'POST'])
def deleteconrtol():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}
    req = request.values
    print(req)
    id = req['id']

    result = Admin.query.filter_by(id=id).first()
    if result.power == '超管':
        resp['msg'] = '禁止操作超管权限'
        return jsonify(resp)
    db.session.delete(result)
    db.session.commit()
    resp['msg'] = '删除成功'
    return jsonify(resp)



