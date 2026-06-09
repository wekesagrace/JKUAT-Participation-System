from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default='admin')

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default='Anonymous')
    message = db.Column(db.Text, nullable=False)
    channel = db.Column(db.String(50), default='web')
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    sentiment = db.Column(db.String(20), default='Pending')
    keywords = db.Column(db.String(300), default='')
    topic = db.Column(db.String(100), default='General')

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    event_date = db.Column(db.String(100), nullable=False)
    event_time = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(100), default='General')
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)