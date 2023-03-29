import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'mysql://root:@localhost/posts'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
