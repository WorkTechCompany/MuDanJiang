APP = {
    'domain': 'http://worktech.xyz'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

AUTH_COOKIE_NAME = 'UserCookie'
SERVER_PORT = '5050'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bryant:leekobe24@cd-cdb-nmj4h99o.sql.tencentcdb.com:63625/app_db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
# SQLALCHEMY_BINDS = {
#     'wechat': 'mysql+pymysql://root:aaaaaaaa@localhost:3306/Mudanjiang'
# }