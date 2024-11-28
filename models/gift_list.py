from .base import db
from datetime import datetime

class GiftList(db.Model):
    __tablename__ = 'gift_lists'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('GiftItem', backref='gift_list', lazy=True)

class GiftItem(db.Model):
    __tablename__ = 'gift_items'
    
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='open')  # 'open' or 'purchased'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    gift_list_id = db.Column(db.Integer, db.ForeignKey('gift_lists.id'), nullable=False)