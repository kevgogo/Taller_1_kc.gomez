import csv
import os
from app.models import db, Guarderia, Cuidador, Perro, Usuario
from app.utils import conditional_print, procesar_password
from config import Config

def cargar_datos_desde_csv():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    archivos_csv = {
        'guarderias': {
            'path': os.path.join(base_dir, '../data/guarderias.csv'),
            'campos': lambda row: Guarderia(
                id=int(row['ID']),
                nombre=row['Nombre'],
                direccion=row['Direccion'],
                telefono=row['Telefono']
            )
        },
        'cuidadores': {
            'path': os.path.join(base_dir, '../data/cuidadores.csv'),
            'campos': lambda row: Cuidador(
                id=int(row['ID']),
                nombre=row['Nombre'],
                telefono=row['Telefono'],
                id_guarderia=int(row['ID_GUARDERIA'])
            )
        },
        'perros': {
            'path': os.path.join(base_dir, '../data/perros.csv'),
            'campos': lambda row: Perro(
                id=int(row['ID']),
                nombre=row['Nombre'],
                raza=row['Raza'],
                edad=int(row['Edad']),
                peso=float(row['Peso']),
                id_guarderia=int(row['ID_GUARDERIA']),
                id_cuidador=int(row['ID_CUIDADOR'])
            )
        }
    }

    for tipo, datos in archivos_csv.items():
        csv_path = datos['path']
        campos = datos['campos']

        conditional_print(f"Cargando datos de {tipo} desde {csv_path}...")
        if not os.path.exists(csv_path):
            conditional_print(f"Archivo {csv_path} no encontrado. Saltando.")
            continue

        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    registro = campos(row)
                    db.session.add(registro)
            conditional_print(f"Datos de {tipo} cargados exitosamente.")
        except Exception as e:
            conditional_print(f"Error al cargar datos de {tipo}: {e}")

    db.session.commit()
    conditional_print("Todos los datos se cargaron exitosamente.")

def inicializar_usuarios():


    # Inicializar usuarios
    admin = Usuario(username='admin', password=procesar_password('admin123'), is_admin=True)
    user = Usuario(username='user',password=procesar_password('user123'))
    test = Usuario(username='test',password=procesar_password('test123'))

    db.session.add_all([admin, user, test])
    db.session.commit()
    conditional_print("Usuarios inicializados.")