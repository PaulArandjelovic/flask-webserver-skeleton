"""Class-based Flask app configuration."""
from os import environ


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = environ.get('FLASK_APP')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # API
    BEST_BUY_API_KEY = environ.get('BEST_BUY_API_KEY')
