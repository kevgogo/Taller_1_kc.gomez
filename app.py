from app import app
from app.utils import conditional_print

def limpiar_proyecto():
    import os
    import shutil

    # Extensiones de bases de datos a eliminar
    extensiones_bd = ['.sqlite', '.db']

    # Recorre todo el proyecto
    for root, dirs, files in os.walk('.'):  # '.' es el directorio actual; cámbialo si es necesario
        # Eliminar directorios __pycache__, excepto los dentro de .venv
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if dir_name == '__pycache__' and '.venv' not in root:
                shutil.rmtree(dir_path)  # Elimina la carpeta __pycache__
                conditional_print(f"Carpeta eliminada: {dir_path}")
            elif dir_name == 'database':
                shutil.rmtree(dir_path)  # Elimina la carpeta database
                conditional_print(f"Carpeta eliminada: {dir_path}")

        # Eliminar archivos de bases de datos
        for file_name in files:
            if any(file_name.endswith(ext) for ext in extensiones_bd):
                file_path = os.path.join(root, file_name)
                os.remove(file_path)  # Elimina el archivo
                conditional_print(f"Archivo de base de datos eliminado: {file_path}")

# Ejecuta la función
if __name__ == '__main__':
    app.run(debug=True)
