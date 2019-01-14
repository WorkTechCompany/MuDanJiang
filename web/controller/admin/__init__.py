from flask import Blueprint, request, jsonify
from common.libs.WebHelper import ops_render
from common.model.admin import Admin

route_admin = Blueprint('admin_page', __name__)
from web.controller.admin.index import *
from web.controller.admin.manager import *
from web.controller.admin.profession import *


@route_admin.route('/', methods=['GET', 'POST'])
@route_admin.route('/login', methods=['GET', 'POST'])
def admin():
    resp = {'code': 200, 'msg': '登录成功'}
    if request.method == 'GET':
        return ops_render('/admin/index.html')

    req = request.values
    name = req['name'] if 'name' in req else ''
    pwd = req['pwd'] if 'pwd' in req else ''

    admin = Admin.query.filter_by(username=name).first()
    admin = Admin.query.filter_by(password=pwd).first()
    resp['id'] = admin.id
    if admin:
        return jsonify(resp)

    resp['code'] = -1

    resp['msg'] = '用户名或密码错误'
    return jsonify(resp)
