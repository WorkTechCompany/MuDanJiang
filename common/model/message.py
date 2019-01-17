from sqlalchemy import Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class message(db.Model):
    __tablename__ = 'message'

    id = db.Column(Integer, primary_key=True)
    category = db.Column(String(100), nullable=False, server_default=FetchedValue())
    mail = db.Column(String(100), nullable=False, server_default=FetchedValue())
    phone = db.Column(String(11), nullable=False, server_default=FetchedValue())
    qq = db.Column(String(20), nullable=False, server_default=FetchedValue())
    title = db.Column(String(50), nullable=False, server_default=FetchedValue())
    content = db.Column(String(5000), nullable=False, server_default=FetchedValue())