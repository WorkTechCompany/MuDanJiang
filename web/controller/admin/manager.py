from web.controller.admin import route_adminfrom common.libs.WebHelper import ops_renderfrom common.model.admin import Adminfrom flask import request, jsonifyfrom application import dbimport time@route_admin.route('/manager', methods=['GET', 'POST'])def manager_index():    resp = {'code': 200, 'info': {}}    req = request.values    id = req['id'] if 'id' in req else -1    if request.method == 'GET':        info = Admin.query.filter_by(id=id).first()        resp['info'] = {            'name': info.username,            'id': id        }        return ops_render('/admin/manager.html', resp)    pwd = req['pwd'] if 'pwd' in req else -1    isadd = req['isadd'] if 'isadd' in req else -1    if isadd == 0:        info = Admin.query.filter_by(id=id).first()    else:        info = Admin()        info.username = req['name']        info.last_time = int(time.time())    info.password = pwd    db.session.add(info)    db.session.commit()    resp['msg'] = '操作成功'    return jsonify(resp)