from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Candidate(db.Model):
    __tablename__ = 'candidates'
    candidate_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    skills = db.Column(db.JSON)
    experience = db.Column(db.JSON)
    education = db.Column(db.JSON)
    resume_url = db.Column(db.String(255))
    source = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class JobPosting(db.Model):
    __tablename__ = 'job_postings'
    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.JSON)
    location = db.Column(db.String(100))
    posted_by = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Application(db.Model):
    __tablename__ = 'applications'
    application_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job_postings.job_id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    score = db.Column(db.Float)
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
