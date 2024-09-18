# Crear un nodo: (dato, siguiente)
def crear_nodo(dato, siguiente=None):
    return (dato, siguiente)

# Insertar un nodo al inicio de la lista
def insertar(cabeza, dato):
    return crear_nodo(dato, cabeza)

# Recorrer la lista
def recorrer(cabeza):
    if cabeza is None:
        return
    print(cabeza[0])
    recorrer(cabeza[1])

# Ejemplo de uso
cabeza = None
cabeza = insertar(cabeza, 3)
cabeza = insertar(cabeza, 2)
cabeza = insertar(cabeza, 1)

recorrer(cabeza) 
