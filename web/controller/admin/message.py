from web.controller.admin import route_admin
from common.libs.WebHelper import ops_render
from common.model.message import message
from application import db
from flask import request, jsonify




@route_admin.route('/controlmsg/', methods=['GET', 'POST'])
def controlmsg():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}
    req = request.values
    page = req['page'] if 'page' in req else 1
    type = req['type'] if 'type' in req else -1
    offset = int(int(page) - 1) * 100
    query = message.query

    if type != -1:
        query = message.query.filter_by(type=type)

    totalCount = query.count()
    list = query.offset(offset).limit(100).all()

    resp['totalCount'] = totalCount
    resp['list'] = list
    resp['pageTotal'] = (totalCount // 100)
    resp['curPage'] = page

    return ops_render('/admin/message.html', resp)


@route_admin.route('/delete_msg/', methods=['GET', 'POST'])
def delete_msg():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}
    req = request.values
    id = req['id']

    result = message.query.filter_by(id=id).first()
    db.session.delete(result)
    db.session.commit()
    resp['msg'] = '删除成功'
    return jsonify(resp)


@route_admin.route('/show_msg/', methods=['GET', 'POST'])
def show_msg():

    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}
    req = request.values
    id = req['id']

    query = message.query.filter_by(id=id).all()
    resp['msg'] = query[0].content

    return jsonify(resp)



