from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.schema import FetchedValue
from application import db


class message(db.Model):
    __tablename__ = 'message'

    id = db.Column(Integer, primary_key=True)
    type = db.Column(Integer, primary_key=True)
    category = db.Column(String(100), nullable=False, server_default=FetchedValue())
    mail = db.Column(String(100), nullable=False, server_default=FetchedValue())
    phone = db.Column(String(11), nullable=False, server_default=FetchedValue())
    messagetime = db.Column(DateTime, nullable=False, index=True, server_default=FetchedValue())
    messagetitle = db.Column(String(100), nullable=False, server_default=FetchedValue())
    content = db.Column(Text, nullable=False, server_default=FetchedValue())