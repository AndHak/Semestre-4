# Funciones de utilidades para el árbol de decisión

def cargar_datos(archivo):
    # Carga los datos del árbol desde un archivo JSON
    import json
    with open(archivo, 'r') as f:
        datos = json.load(f)
    return datos
