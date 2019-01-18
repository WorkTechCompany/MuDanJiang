from web.controller.admin import route_adminfrom common.libs.WebHelper import ops_renderfrom common.model.data import datafrom common.model.classify import classifyfrom common.libs.UrlManager import UrlManagerfrom flask import request, jsonify, redirectfrom application import db, appimport os@route_admin.route('/profession', methods=['GET', 'POST'])def profession_index():    resp = {'code': 200, 'info': {}}    req = request.values    #    if request.method == 'GET':        try:            id = req['id']            info = data.query.filter_by(id=id).first()            resp['info'] = {                'id': id,                'title': info.title,                'f0': info.f0_desc,                'f1': info.f1_desc,                'f2': info.f2_desc,                'time': info.time,                "url": info.url,                "image": info.image,                "content": info.content,                "content_url": info.content_url,                "Introduction": info.Introduction,                "content_title": info.content_title            }            return ops_render('/admin/profession.html', resp)        except:            return ops_render('/admin/profession.html', resp)@route_admin.route('/update', methods=['GET', 'POST'])def update():    id = request.values['id'] if 'id' in request.values else -1    summnerNote = {}    if id != -1 and id:        summnerNote = data.query.filter_by(id=id).first()    else:        summnerNote = data()    f0 = request.values['f0']    f1 = request.values['f1']    f2 = request.values['f2']    # print(request.values)    summnerNote.title = request.values['title'] if 'title' in request.values else ''    summnerNote.content = request.values['content'] if 'content' in request.values else ''    summnerNote.time = request.values['time'] if 'time' in request.values else ''    summnerNote.content_url = request.values['content_url'] if 'content_url' in request.values else ''    summnerNote.url = request.values['url'] if 'url' in request.values else ''    summnerNote.Introduction = request.values['Introduction'] if 'Introduction' in request.values else ''    summnerNote.content_title = request.values['content_title'] if 'content_title' in request.values else ''    type = 1  # 是视频    if summnerNote.content_url == '空' or summnerNote.content_url == '':        type = 0  # 不是视频    if f0 != '/':        get_f0 = classify.query.filter_by(name=f0).first().did    else:        get_f0 = -1    if f1 != '/':        get_f1 = classify.query.filter_by(name=f1).first().did    else:        get_f1 = -1    if f2 != '/':        get_f2 = classify.query.filter_by(name=f2).first().did    else:        get_f2 = -1    summnerNote.f0 = get_f0    summnerNote.f1 = get_f1    summnerNote.f2 = get_f2    summnerNote.type = type    try:        image = request.files['image']        file_path = os.path.join('Images/', image.filename)        save_path = os.path.join(app.config["ABS_UPLOAD_FOLDER"], image.filename)        image.save(save_path)        summnerNote.image = file_path        db.session.add(summnerNote)        db.session.commit()        if id == -1:            id = summnerNote.id            return redirect(UrlManager.buildUrl("/admin/profession?id=" + str(id)))        else:            id = summnerNote.id            return redirect(UrlManager.buildUrl("/admin/profession?id=" + str(id)))    except:        db.session.add(summnerNote)        db.session.commit()        if id == -1:            id = summnerNote.id            return redirect(UrlManager.buildUrl("/admin/profession?id=" + str(id)))        else:            id = summnerNote.id            return redirect(UrlManager.buildUrl("/admin/profession?id=" + str(id)))@route_admin.route('/upload_img/', methods=['POST'])def summernote_image():    response = {'status': 1, 'message': '文件上传成功'}    image = request.files['file']    file_path = os.path.join('Images/', image.filename)    save_path = os.path.join(app.config["ABS_UPLOAD_FOLDER"], image.filename)    image.save(save_path)    result = UrlManager.buildImageUrl(file_path)    response['img'] = result    return jsonify(response)# @route_admin.route('/ops')# def summernot_ops():#     # resp = {'code': 200, 'totalCount': 0, 'pageTotal': 0, 'list': {}, 'curPage': 1}##     id = request.values['id'] if id in request else -1##     summnerNote = {}#     if id == -1:#         summnerNote = data.query.filter_by(id=id).first()#     else:#         summnerNote = data()##     f0 = request.values['f0']#     f1 = request.values['f1']#     f2 = request.values['f2']#     summnerNote.title = request.values['title'] if 'title' in request.values else ''#     summnerNote.content = request.values['content'] if 'content' in request.values else ''#     summnerNote.time = request.values['time'] if 'time' in request.values else ''#     summnerNote.content_url = request.values['content_url'] if 'content_url' in request.values else ''#     summnerNote.url = request.values['url'] if 'url' in request.values else ''#     summnerNote.Introduction = request.values['Introduction'] if 'Introduction' in request.values else ''#     summnerNote.content_title = request.values['content_title'] if 'content_title' in request.values else ''#     type = 1  # 是视频##     if summnerNote.content_url == '空' or summnerNote.content_url == '':#         type = 0  # 不是视频##     if f0 != '/':#         get_f0 = classify.query.filter_by(name=f0).first().did#     else:#         get_f0 = -1#     if f1 != '/':#         get_f1 = classify.query.filter_by(name=f1).first().did#     else:#         get_f1 = -1#     if f2 != '/':#         get_f2 = classify.query.filter_by(name=f2).first().did#     else:#         get_f2 = -1##     summnerNote.f0 = get_f0#     summnerNote.f1 = get_f1#     summnerNote.f2 = get_f2#     summnerNote.type = type##     image = request.files['image']#     if image:#         file_path = os.path.join('Images/', image.filename)#         save_path = os.path.join(app.config["ABS_UPLOAD_FOLDER"], image.filename)#         image.save(save_path)#         summnerNote.image = file_path##     db.session.add(summnerNote)#     db.session.commit()##     if id == -1:#         id = summnerNote.id#         return redirect(UrlManager.buildUrl("/admin/profession?id=" + str(id)))#     else:#         return redirect(UrlManager.buildUrl("/admin/profession?id=" + str(id)))