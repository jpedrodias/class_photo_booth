import os
import redis


class BaseConfig():
    """Base configuration class."""
    DEBUG = os.getenv('FLASKAPP_DEBUG', 'True').lower() in ['true', '1', 'yes']
    TESTING = False

    
    # SESSIONS on FILE » MUITO LENTO em TESTES
    #SESSION_COOKIE_NAME = 'flaskapp_session'
    #SESSION_TYPE = 'filesystem'
    #SESSION_FILE_DIR = os.path.join(os.path.dirname(__file__), 'session_files')
    #SESSION_FILE_MODE = 600
    #SESSION_FILE_THRESHOLD = 2000

    # SESSIONS on REDIS
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url("redis://redis:6379/0")
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'session:'
    SESSION_SERIALIZATION_FORMAT = 'msgpack'  # Usar msgpack para melhor compatibilidade

    # Chaves e URIs
    SECRET_KEY = os.getenv('FLASKAPP_SECRET_KEY', 'supersecretkey')
    LOGIN_PIN = os.getenv('FLASKAPP_LOGIN_PIN', '1234')
    DATABASE_URI = os.getenv('FLASKAPP_DATABASE_URL', 'sqlite:///database.sqlite')

    # Configurações do SQLAlchemy
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Diretórios para fotos e miniaturas
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PHOTOS_DIR = os.path.join(BASE_DIR, 'photos_originals')
    THUMBS_DIR = os.path.join(BASE_DIR, 'photos_thumbs')

    # Configurações de email
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'email@email.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '1234')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_SENDER', f'Class Photo Booth <{os.getenv("MAIL_USERNAME", "email@email.com")}>')
    MAIL_DEBUG = False
# End class BaseConfig


class DevelopmentConfig(BaseConfig):
    """Development configuration class."""
    DEBUG = True
# End class DevelopmentConfig


class ProductionConfig(BaseConfig):
    """Production configuration class."""
    DEBUG = False
# End class ProductionConfig
