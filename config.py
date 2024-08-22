import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/ats_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NAUKRI_API_KEY = os.environ.get('NAUKRI_API_KEY') or '12345678-ABCD-1234-EFGH-567890IJKLMP'
