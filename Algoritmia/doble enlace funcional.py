# Crear un nodo: (dato, anterior, siguiente)
def crear_nodo(dato, anterior=None, siguiente=None):
    return (dato, anterior, siguiente)

# Insertar un nodo al inicio de la lista
def insertar(cabeza, dato):
    nuevo_nodo = crear_nodo(dato, None, cabeza)
    if cabeza:
        cabeza = (cabeza[0], nuevo_nodo, cabeza[2])
    return nuevo_nodo

# Recorrer la lista hacia adelante
def recorrer_adelante(cabeza):
    if cabeza is None:
        return
    print(cabeza[0])
    recorrer_adelante(cabeza[2])

# Recorrer la lista hacia atrás
def recorrer_atras(cola):
    if cola is None:
        return
    print(cola[0])
    recorrer_atras(cola[1])

# Ejemplo de uso
cabeza = None
cabeza = insertar(cabeza, 3)
cabeza = insertar(cabeza, 2)
cabeza = insertar(cabeza, 1)

recorrer_adelante(cabeza) 
print("")
recorrer_atras(cabeza)

