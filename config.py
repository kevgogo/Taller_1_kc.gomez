import os
import secrets
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(32))
    APP_ENV = os.getenv('APP_ENV', 'development')
    ENABLE_PRINTS = os.getenv('ENABLE_PRINTS', 'false').lower() == 'true'
    ENCRYPT_PASSWORDS = os.getenv('ENCRYPT_PASSWORDS', 'true').lower() == 'true'

    # Database Configuration
    DB_TYPE = os.getenv('DB_TYPE', 'sqlite')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DB = os.getenv('MYSQL_DB', 'TABLAS')
    SQLITE_DB = os.getenv('SQLITE_DB', 'tablas')  # Default SQLite database name

    @staticmethod
    def database_uri(isFirstTime=False):
        basedir = os.path.abspath(os.path.dirname(__file__))
        os.makedirs(os.path.join(basedir, "database"), exist_ok=True)
        db_path = os.path.join(basedir, "database", "heladeria.db")

        if Config.DB_TYPE == 'mysql':
            if isFirstTime:
                return f"mysql+pymysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}"
            return f"mysql+pymysql://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{Config.MYSQL_DB}"
        return f"sqlite:///{db_path}"