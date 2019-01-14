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


#
# CREATE TABLE `data` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `l_t_id` int(11) DEFAULT NULL,
#   `m_t_id` int(11) DEFAULT NULL,
#   `s_t_id` int(11) DEFAULT NULL,
#   `title` varchar(11) DEFAULT NULL,
#   `time` datetime DEFAULT NULL,
#   PRIMARY KEY (`id`) USING BTREE,
#   UNIQUE KEY `id` (`id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;