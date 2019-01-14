from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class Profession(db.Model):
    __tablename__ = 'profession'

    pid = db.Column(Integer, primary_key=True)
    p_name = db.Column(String(100), nullable=False, server_default=FetchedValue())
    flg = db.Column(Integer, nullable=False, server_default=FetchedValue())
    url = db.Column(String(128), nullable=False, server_default=FetchedValue())
    time = db.Column(String(128), nullable=False, server_default=FetchedValue())