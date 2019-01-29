from web.controller.admin import route_admin
from common.libs.WebHelper import ops_render
from common.model.admin import Admin

from flask import request, jsonify
from application import db

import time


@route_admin.route('/changepwd/', methods=['GET', 'POST'])
def changepwd():
    resp = {'code': 200, 'info': {}}
    req = request.values
    if request.method == 'GET':
        return ops_render('/admin/changepwd.html', resp)

    username = req['username']
    password = req['password']

    data = Admin.query.filter_by(username=username).first()
    data.password = password
    db.session.commit()
    resp['msg'] = '操作成功'
    return jsonify(resp)
