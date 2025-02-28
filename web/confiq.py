
from os import getenv

TESTING = getenv('TESTING') 
DEBUG = getenv('DEBUG') 
FLASK_ENV = getenv('FLASK_ENV')

# email config
MAIL_DEBUG = 1
DEFAULT_MAIL_SENDER = getenv('MAIL_USERNAME') or "hi@techa.tech"
SECRET_KEY = getenv('SECRET_KEY') or 'you-will-never-guess-usssss'

# Set the SQLALCHEMY_DATABASE_ENGINE option
SQLALCHEMY_DATABASE_ENGINE = {
    'rollback_on_exception': True,
}

SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 50   # Increase the pool size if necessary
SQLALCHEMY_POOL_TIMEOUT = 30  # Increase the pool timeout if necessary
SQLALCHEMY_MAX_OVERFLOW = 20  # Allow up to 20 additional connections beyond the pool size

""" 
SQLALCHEMY_POOL_RECYCLE = 3600  # Recycle connections every hour
 """
 
LOG_TO_STDOUT = getenv('LOG_TO_STDOUT')

""" ===========                      ======="""
MAIL_PORT = int(getenv('MAIL_PORT', 587))  # Ensure this is an integer
MAIL_USE_TLS = bool(str(getenv('MAIL_USE_TLS', 'True')))  # ensure type is compatible to avoid Flask-Mail [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1123)
MAIL_USE_SSL = bool(getenv('MAIL_USE_SSL', 'False'))

DEFAULT_MAIL_SENDER = (getenv('DEFAULT_MAIL_SENDER'), 'Intellect') 
MAIL_SERVER = getenv('MAIL_SERVER')
MAIL_USERNAME = getenv('MAIL_USERNAME')
MAIL_PASSWORD = getenv('MAIL_PASSWORD')
""" ============              ======== """
    
ADMINS = ['jameschristo962@gmail.com', 'chrisjsmez@gmail.com']
LANGUAGES = ['en', 'es']
MS_TRANSLATOR_KEY = getenv('MS_TRANSLATOR_KEY')
ELASTICSEARCH_URL = getenv('ELASTICSEARCH_URL')
POSTS_PER_PAGE = 25

UPLOAD_FOLDER = getenv('UPLOAD_FOLDER')
#Specifies the maximum size (in bytes) of the files to be uploaded
MAX_CONTENT_PATH = getenv('MAX_CONTENT_PATH')
ALLOWED_EXTENSIONS = getenv('ALLOWED_EXTENSIONS')
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
MAX_CONTENT_LENGTH = 1024 * 1024

#prevents Shared Session Cookies
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True  # If using HTTPS
SESSION_TYPE = 'filesystem'
