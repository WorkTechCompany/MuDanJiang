from application import db, app
from flask import Blueprint, request, g, jsonify, redirect
from common.libs.WebHelper import ops_render
from common.model.department import Department
from common.model.classify import classify
from common.model.profession import Profession
from common.libs.WechatService import WeChatService
import time, asyncio, requests, json

route_index = Blueprint('index_page', __name__)
loop = asyncio.get_event_loop()

wechat = WeChatService()

@route_index.route('/')
@route_index.route('/index')
def index():
    return ops_render('/admin/index.html')


@route_index.route('/next')
def index_next():
    resp = {}
    req = request.values
    id = req['id'] if 'id' in req else 0
    openId = req['openId'] if 'openId' in req else 0

    resp['profession'] = Profession.query.order_by(Profession.pid.desc()).first()
    info = Department.query.filter_by(did=id).first()
    list = Department.query.filter_by(fid=id).all()

    resp['list'] = list
    resp['info'] = info
    resp['openId'] = openId
    resp['share'] = wechat.getShareData()
    return ops_render('index_next.html', resp)


@route_index.route('/f1')
def f1():
    req = request.values
    id = req['id'] if 'id' in req else -1

    list = classify.query.filter_by(fid=id).all()
    resp = {}
    resp['list'] = list
    tmp_data = []
    for item in list:
        resp = {
            'did': item.did,
            'd_name': item.name,
            'fid': item.fid,
            'flg': item.flg
        }
        tmp_data.append(resp)

    return jsonify(tmp_data)


@route_index.route('/test')
def test():
    loop.run_until_complete(SignUp())
    return '报名成功1234'


async def SignUp():
    time.sleep(5)