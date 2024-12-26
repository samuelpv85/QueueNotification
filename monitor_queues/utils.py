import os

def ensure_directory_exists(path):
    """Asegura que el directorio para una ruta exista."""
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
