from app import db
from .base import Base

class User(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile_no = db.Column(db.String(50), unique=True, nullable=False)
    discussions = db.relationship('Discussion', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='commenter', lazy='dynamic')
    likes = db.relationship('Like', backref='liker', lazy='dynamic')
    followed = db.relationship(
        'Follow', foreign_keys='Follow.follower_id',
        backref='follower', lazy='dynamic', cascade='all, delete-orphan'
    )
    followers = db.relationship(
        'Follow', foreign_keys='Follow.followed_id',
        backref='followed', lazy='dynamic', cascade='all, delete-orphan'
    )