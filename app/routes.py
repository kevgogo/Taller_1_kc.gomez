from flask import abort, render_template, request, session
from app import app, db
from app.models import Perro, Cuidador, Guarderia
from app.utils import login_required

@app.route('/')
@login_required
def index():
    is_admin = session.get('is_admin', False)
    return render_template('index.html' if is_admin else 'saludo.html', mensaje="¡Bienvenido al sistema!")

@app.route('/buscar_lassie')
@login_required
def buscar_lassie():
    cantidad_lassie = Perro.query.filter_by(nombre='Lassie').count()
    return render_template('buscar_lassie.html', cantidad=cantidad_lassie)

@app.route('/asignar_perros_a_mario')
@login_required
def asignar_perros_a_mario():
    if not session.get('is_admin'):  # Verifica si el usuario es administrador
        abort(403)  # Lanza un error 403 si no tiene permisos

    # Lógica de asignación
    mario = Cuidador.query.filter_by(nombre='Mario').first()
    if not mario:
        mario = Cuidador(nombre='Mario', telefono='111-2222')
        db.session.add(mario)
        db.session.commit()

    perros_pequenos = Perro.query.filter(Perro.peso < 3).all()
    for perro in perros_pequenos:
        perro.cuidador = mario
    db.session.commit()

    return render_template('asignar_perros.html', cantidad=len(perros_pequenos))

@app.route('/perros_de_mario')
@login_required
def perros_de_mario():
    mario = Cuidador.query.filter_by(nombre='Mario').first()
    if not mario:
        return "Mario no se encuentra en la base de datos", 404

    perros = mario.perros
    return render_template('perros_de_mario.html', mario=mario, perros=perros)

@app.route('/guarderia_favorita')
@login_required
def guarderia_favorita():
    if not session.get('is_admin'):  # Verifica si el usuario es administrador
        abort(403)  # Lanza un error 403 si no tiene permisos

    guarderia = Guarderia.query.filter_by(nombre="La Favorita").first()
    if not guarderia:
        return "La guardería 'La Favorita' no se encuentra en la base de datos", 404

    cuidadores = guarderia.cuidadores
    return render_template('guarderia_favorita.html', guarderia=guarderia, cuidadores=cuidadores)

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html', path=request.path), 404

@app.errorhandler(403)
def acceso_prohibido(e):
    return render_template('403.html', mensaje="No tienes permisos suficientes para esta acción."), 403