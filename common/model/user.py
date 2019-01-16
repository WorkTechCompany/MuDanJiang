from sqlalchemy import Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class user(db.Model):
    __tablename__ = 'user'

    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(100), nullable=False, server_default=FetchedValue())
    userpassword = db.Column(String(128), nullable=False, server_default=FetchedValue())
    mail = db.Column(String(128), nullable=False, server_default=FetchedValue())