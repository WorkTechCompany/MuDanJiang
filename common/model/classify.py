from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db
import datetime


class classify(db.Model):
    __tablename__ = 'classify'

    did = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False, server_default=FetchedValue())
    fid = db.Column(Integer, nullable=False, server_default=FetchedValue())
    flg = db.Column(Integer, nullable=False, server_default=FetchedValue())
