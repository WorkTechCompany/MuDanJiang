from sqlalchemy import Integer, String
from sqlalchemy.schema import FetchedValue
from application import db
from common.model.classify import classify


class data(db.Model):
    __tablename__ = 'data'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(100), nullable=False, server_default=FetchedValue())
    f0 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f1 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f2 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    image = db.Column(String(100), nullable=False, server_default=FetchedValue())
    url = db.Column(String(100), nullable=False, server_default=FetchedValue())
    content = db.Column(String(100000), nullable=False, server_default=FetchedValue())
    time = db.Column(String(100), nullable=False, server_default=FetchedValue())
    content_url = db.Column(String(100), nullable=False, server_default=FetchedValue())
    Introduction = db.Column(String(1000), nullable=False, server_default=FetchedValue())
    content_title = db.Column(String(100), nullable=False, server_default=FetchedValue())
    type = db.Column(Integer, nullable=False, server_default=FetchedValue())



    @property
    def f0_desc(self):
        de = classify.query.filter_by(did=self.f0).first()
        return de.name

    @property
    def f1_desc(self):
        de = classify.query.filter_by(did=self.f1).first()
        if de:
            return de.name
        else:
            return '/'

    @property
    def f2_desc(self):
        de = classify.query.filter_by(did=self.f2).first()
        if de:
            return de.name
        else:
            return '/'