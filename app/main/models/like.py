from datetime import datetime
from app import db
from .base import Base


class Like(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    discussion_id = db.Column(db.Integer, db.ForeignKey('discussion.id', ondelete="CASCADE"), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id', ondelete="CASCADE"), nullable=True)
