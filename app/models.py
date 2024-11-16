from app.extensions import db

class Guarderia(db.Model):
    __tablename__ = 'guarderias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    cuidadores = db.relationship('Cuidador', backref='guarderia', lazy=True)
    perros = db.relationship('Perro', backref='guarderia', lazy=True)

class Cuidador(db.Model):
    __tablename__ = 'cuidadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.id'))
    perros = db.relationship('Perro', backref='cuidador', lazy=True)

class Perro(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Float)
    id_guarderia = db.Column(db.Integer, db.ForeignKey('guarderias.id'))
    id_cuidador = db.Column(db.Integer, db.ForeignKey('cuidadores.id'))

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Campo para roles