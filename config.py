# import os

# # Flask Configuration
# class Config:
#     """Base configuration for Flask"""
#     SECRET_KEY = os.getenv('SECRET_KEY', 'inventorymanagment')
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     DEBUG = True

# # Environment dictionary for easy switching
# config = {
#     'development': Config
# }

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "inventory.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

