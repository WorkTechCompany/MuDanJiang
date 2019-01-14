from flask import Blueprint, request
from common.model.data import data


route_getinfo = Blueprint('getinfo', __name__)
@route_getinfo.route('/getinfo', methods=['POST'])
def post(self):
    '''
    f0：
    f1:
    f2:

    :return:
    '''
    req = request.values
    f0 = req['f0'] if 'f0' in req else -1
    f1 = req['f1'] if 'f1' in req else -1
    f2 = req['f2'] if 'f2' in req else -1

    if f0 != -1:
        query = data.query.filter_by(f0=f0)
    if f1 != '-1':
        query = data.query.filter_by(f1=f1)
    if f2 != '-1':
        query = data.query.filter_by(f2=f2)

    result = query.all()
    print(result)


    return 'success'


