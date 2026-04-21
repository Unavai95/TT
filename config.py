import os

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max file size limit to 16 MB

    # Upload folder
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

    # Other application settings
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
