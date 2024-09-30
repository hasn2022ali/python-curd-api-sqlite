import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'hassan-ali-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
