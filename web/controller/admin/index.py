from web.controller.admin import route_adminfrom common.libs.WebHelper import ops_renderfrom common.model.user import userfrom common.model.data import datafrom common.model.message import messagefrom flask import request, jsonifyfrom common.libs.UrlManager import UrlManagerfrom common.model.classify import classifyfrom common.libs.WebHelper import getFormatDatefrom application import dbfrom sqlalchemy import or_@route_admin.route('/index/', methods=['GET', 'POST'])def admin_index():    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}    req = request.values    page = req['page'] if 'page' in req else 1    f0 = req['f0'] if 'f0' in req else -1    f1 = req['f1'] if 'f1' in req else -1    f2 = req['f2'] if 'f2' in req else -1    offset = int(int(page) - 1) * 100    query = data.query    if f0 != -1:        query = data.query.filter_by(f0=f0)    if f1 != 'null' and f1 != -1:        query = data.query.filter_by(f1=f1)    if f2 != 'null' and f2 != -1:        query = data.query.filter_by(f2=f2)    totalCount = query.count()    list = query.offset(offset).limit(100).all()    resp['totalCount'] = totalCount    resp['list'] = list    resp['pageTotal'] = (totalCount // 100) + 1    resp['curPage'] = page    resp['f0'] = f0    resp['f1'] = f1    resp['f2'] = f2    return ops_render('/admin/apply.html', resp)@route_admin.route('/delete', methods=['GET', 'POST'])def show_content():    resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}    req = request.values    id = req['id']    result = data.query.filter_by(id=id).first()    db.session.delete(result)    db.session.commit()    resp['msg'] = '删除成功'    return jsonify(resp)@route_admin.route('/getinfo/', methods=['GET', 'POST'])def post():    response = {'code': 200, 'msg': '查询成功'}    req = request.values    f0 = req['f0'] if 'f0' in req else -1    f1 = req['f1'] if 'f1' in req else -1    try:        f2 = req['f2']        if f0 != -1:            query = data.query.filter_by(f0=f0)        if f1 != '-1':            query = data.query.filter_by(f1=f1)        if f2 != '-1':            query = data.query.filter_by(f2=f2)    except:        if f0 != -1:            query = data.query.filter_by(f0=f0)        if f1 != '-1':            query = data.query.filter_by(f1=f1)    result = query.all()    tmp_list = []    for item in result:        tmp_data = {            'id': item.id,            'title': item.title,            'time': getFormatDate(item.time),            'image': UrlManager.buildImageUrl(item.image),            'url': item.url,            'Introduction': item.Introduction,            'content_url': item.content_url,            'type': item.type        }        tmp_list.append(tmp_data)    response['list'] = tmp_list    resp = jsonify(response)    resp.headers['Access-Control-Allow-Origin'] = '*'    return resp@route_admin.route('/getinfo/getcontent/', methods=['GET', 'POST'])def post_content():    response = {'code': 200, 'msg': '查询成功'}    req = request.values    id = req['id'] if 'id' in req else -1    query = data.query.filter_by(id=id)    result = query.all()    tmp_list = []    for item in result:        tmp_data = {            'id': item.id,            'title': item.title,            'content': item.content,            'content_url': item.content_url,            'content_title': item.content_title        }        tmp_list.append(tmp_data)    response['result'] = tmp_list    resp = jsonify(response)    resp.headers['Access-Control-Allow-Origin'] = '*'    return resp@route_admin.route('/userlogin/', methods=['POST'])def login():    response = {'code': 200, 'msg': '登录成功'}    req = request.values    username = req['username']    userpassword = req['userpassword']    query = user.query.filter_by(username=username)    result = query.all()    if len(result) == 0:        response['code'] = -1        response['msg'] = '用户名或密码错误'        resp = jsonify(response)        resp.headers['Access-Control-Allow-Origin'] = '*'        return resp    password = result[0].userpassword    if password == userpassword:        resp = jsonify(response)        resp.headers['Access-Control-Allow-Origin'] = '*'        return resp    else:        response['code'] = -1        response['msg'] = '用户名或密码错误'        resp = jsonify(response)        resp.headers['Access-Control-Allow-Origin'] = '*'        return resp@route_admin.route('/sign_up/', methods=['POST'])def sign_up():    response = {'code': 200, 'msg': '注册成功'}    req = request.values    username = req['username']    query = user.query.filter_by(username=username)    result = query.all()    if len(result) != 0:        response['code'] = -1        response['msg'] = '用户名已存在'        resp = jsonify(response)        resp.headers['Access-Control-Allow-Origin'] = '*'        return resp    try:        userpassword = req['userpassword']        mail = req['mail']        add_user = user(username=username, userpassword=userpassword, mail=mail)        db.session.add(add_user)        db.session.commit()        resp = jsonify(response)        resp.headers['Access-Control-Allow-Origin'] = '*'        return resp    except:        response['msg'] = '用户名可用'        resp = jsonify(response)        resp.headers['Access-Control-Allow-Origin'] = '*'        return resp@route_admin.route('/message/', methods=['POST'])def send_message():    response = {'code': 200, 'msg': '发表成功'}    req = request.values    category = req['category']    mail = req['mail']    phone = req['phone']    content = req['content']    if category == '普通':        type = 2    else:        type = 1    add_message = message(category=category, mail=mail, phone=phone, content=content, type=type)    db.session.add(add_message)    db.session.commit()    resp = jsonify(response)    resp.headers['Access-Control-Allow-Origin'] = '*'    return resp@route_admin.route('/search/', methods=['POST'])def search():    response = {'code': 200, 'msg': '查询成功'}    result = request.values    tmp_list = []    info = result['info']    condition = '%' + info + '%'    result = data.query.filter(or_(data.title.like(condition), data.content.like(condition))).all()    for item in result:        # if item.url != '空' and item.url != None:        #     continue        try:            get_f1 = classify.query.filter_by(did=item.f1).first().name        except:            get_f1 = ''        tmp_data = {            'id': item.id,            'title': item.title,            'category': get_f1,            'content': item.content,            'time': item.time,            'type': item.type        }        tmp_list.append(tmp_data)    response['result'] = tmp_list    resp = jsonify(response)    resp.headers['Access-Control-Allow-Origin'] = '*'    return resp