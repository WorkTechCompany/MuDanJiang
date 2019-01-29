from flask import Blueprint, request, jsonify
from common.libs.WebHelper import ops_render
from common.model.admin import Admin
from web.controller.admin.utils import create_folder

route_admin = Blueprint('admin_page', __name__)
from web.controller.admin.index import *
from web.controller.admin.manager import *
from web.controller.admin.profession import *
from web.controller.admin.message import *
from web.controller.admin.userinfo import *
from web.controller.admin.count import *
from web.controller.admin.control import *
from web.controller.admin.changepwd import *

# app.config['UPLOAD_FOLDER'] = "Images"
#
# create_folder(app.config['UPLOAD_FOLDER'])


@route_admin.route('/', methods=['GET', 'POST'])
@route_admin.route('/login', methods=['GET', 'POST'])
def admin():
    resp = {'code': 200, 'msg': '登录成功'}
    if request.method == 'GET':
        return ops_render('/admin/index.html')

    req = request.values
    name = req['name'] if 'name' in req else ''
    pwd = req['pwd'] if 'pwd' in req else ''


    name_1 = Admin.query.filter_by(username=name).first()

    if name_1 == None:
        resp['code'] = -1
        resp['msg'] = '用户名或密码错误'
        return jsonify(resp)
    if pwd == name_1.password:
        resp['power'] = name_1.power
        resp['username'] = name_1.username
        return jsonify(resp)
    resp['code'] = -1
    resp['msg'] = '用户名或密码错误'
    return jsonify(resp)
