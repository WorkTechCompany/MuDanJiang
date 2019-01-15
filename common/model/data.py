from sqlalchemy import Column, DateTime, Integer, String
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
    content = db.Column(String(5000), nullable=False, server_default=FetchedValue())
    time = db.Column(String(100), nullable=False, server_default=FetchedValue())
    content_image = db.Column(String(100), nullable=False, server_default=FetchedValue())
    content_url = db.Column(String(100), nullable=False, server_default=FetchedValue())
    Introduction = db.Column(String(100), nullable=False, server_default=FetchedValue())
    content_title = db.Column(String(100), nullable=False, server_default=FetchedValue())


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





# CREATE TABLE `data` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `title` varchar(255) NOT NULL,
#   `f1` int(11) NOT NULL,
#   `f2` int(11) NOT NULL,
#   `f3` int(11) NOT NULL,
#   `time` datetime NOT NULL,
#   PRIMARY KEY (`id`) USING BTREE,
#   UNIQUE KEY `id` (`id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;