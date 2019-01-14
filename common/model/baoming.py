from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from common.model.department import Department
from common.model.profession import Profession
from application import db


class BaoMing(db.Model):
    __tablename__ = 'baoming'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False, server_default=FetchedValue())
    sid = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f1 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f2 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f3 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f4 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    f0 = db.Column(Integer, nullable=False, server_default=FetchedValue())
    openid = db.Column(String(128), nullable=False, server_default=FetchedValue())

    @property
    def sid_desc(self):
        pro = Profession.query.order_by(Profession.pid.desc()).first()
        return pro.p_name

    @property
    def f0_desc(self):
        de = Department.query.filter_by(did=self.f0).first()
        return de.d_name

    @property
    def f1_desc(self):
        de = Department.query.filter_by(did=self.f1).first()
        return de.d_name

    @property
    def f2_desc(self):
        de = Department.query.filter_by(did=self.f2).first()
        return de.d_name

    @property
    def f3_desc(self):
        de = Department.query.filter_by(did=self.f3).first()
        return de.d_name

    @property
    def f4_desc(self):
        de = Department.query.filter_by(did=self.f4).first()
        return de.d_name
