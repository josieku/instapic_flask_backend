
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt

class Post(db.Model):
    """ Post Model for storing an image and description"""
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String())
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', foreign_keys=user_id, lazy='select')
    posted_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Post '{}'>".format(self.id)
