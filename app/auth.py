from flask import flash, request, render_template, redirect, url_for, session, Response
from app import app
from app.models import Usuario
from app.utils import comparar_password
from config import Config

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Usuario.query.filter_by(username=username).first()

        if user and comparar_password(password, user.password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin  # Solo campos simples
            flash('Inicio de sesión exitoso', 'success')

            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    usuarios = Usuario.query.all()
    return render_template('login.html', usuarios=usuarios, encrypt_passwords=Config.ENCRYPT_PASSWORDS)

@app.route('/login', methods=['GET'])
def mostrar_login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    response = redirect(url_for('login'))
    for cookie in request.cookies:
        response.delete_cookie(cookie)
    return response