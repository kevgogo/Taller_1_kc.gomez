import shutil
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text, inspect
from pymysql import OperationalError

from app.extensions import db
from app.data_loader import cargar_datos_desde_csv, inicializar_usuarios
from app.utils import conditional_print
from config import Config


app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.secret_key = Config.SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Step 1: Create database if it doesn't exist
if Config.DB_TYPE == 'mysql':
    temp_engine = create_engine(Config.database_uri(isFirstTime=True))
    try:
        with temp_engine.connect() as connection:
            connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DB}"))
            conditional_print(f"Database '{Config.MYSQL_DB}' created or already exists.")
    except OperationalError as e:
        conditional_print(f"Error creating database: {e}")
    finally:
        temp_engine.dispose()

app.config['SQLALCHEMY_DATABASE_URI'] = Config.database_uri(isFirstTime=False)
conditional_print(f"Final SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

db.init_app(app)
conditional_print("SQLAlchemy initialized successfully.")

# Step 3: Debug database connection and inspector
with app.app_context():
    try:
        connection = db.engine.connect()
        conditional_print("Database connection successful.")
        connection.close()
    except Exception as e:
        conditional_print(f"Database connection failed: {e}")

    try:
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        if tables:
            conditional_print(f"Existing tables: {tables}")
            db.drop_all()  # Drop existing tables for a fresh start
        else:
            conditional_print("No tables found. Ready to create tables.")
        db.create_all()  # Create tables from SQLAlchemy models
        cargar_datos_desde_csv()
        inicializar_usuarios()
    except Exception as e:
        conditional_print(f"Error with inspector or database operations: {e}")

from app import auth, routes