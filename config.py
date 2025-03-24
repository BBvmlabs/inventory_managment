import os
from dotenv import load_dotenv

load_dotenv()
# Flask Configuration.
class Config:
    """Base configuration for Flask"""
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = os.getenv('DEBUG')

# Environment dictionary for easy switching
config = {
    'development': Config
}
