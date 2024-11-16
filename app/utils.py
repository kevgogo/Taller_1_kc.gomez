from flask import flash, session, redirect, url_for, request
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  
            flash("Debes iniciar sesión para acceder a esta página.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def conditional_print(message):
    if Config.ENABLE_PRINTS:
        print(message)

def procesar_password(password):
    if Config.ENCRYPT_PASSWORDS:
        return generate_password_hash(password, method='pbkdf2:sha256')
    return password

def comparar_password(password, hashed_password):
    if Config.ENCRYPT_PASSWORDS:
        return check_password_hash(hashed_password, password)
    return hashed_password == password
