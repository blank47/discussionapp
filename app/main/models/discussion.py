from datetime import datetime
from app import db
from .base import Base


class Discussion(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(300), nullable=True)
    created_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='discussion', lazy='dynamic')
    hashtags = db.Column(db.String(300), nullable=True)  # Store hashtags as a single string
    likes = db.relationship('Like', backref='discussion', lazy='dynamic')
