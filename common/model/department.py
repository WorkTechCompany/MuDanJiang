from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class Department(db.Model):
    __tablename__ = 'departments'

    did = db.Column(Integer, primary_key=True)
    d_name = db.Column(String(100), nullable=False, server_default=FetchedValue())
    fid = db.Column(Integer, nullable=False, server_default=FetchedValue())
    flg = db.Column(Integer, nullable=False, server_default=FetchedValue())
    num = db.Column(Integer, nullable=False, server_default=FetchedValue())
    joinnum = db.Column(Integer, nullable=False, server_default=FetchedValue())
    joinpercent = db.Column(Integer, nullable=False, server_default=FetchedValue())
