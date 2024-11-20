
class NodoDecision:
    def __init__(self, criterio, valor, hijos=None, es_hoja=False, clasificacion=None):
        # Criterio del nodo de decisión (atributo de decisión, ej., "edad")
        self.criterio = criterio
        # Valor del criterio que define este nodo (ej., "Menor de 18 años")
        self.valor = valor
        # Lista de nodos hijos si no es una hoja
        self.hijos = hijos or []
        # Booleano para indicar si el nodo es una hoja
        self.es_hoja = es_hoja
        # Clasificación asignada si es hoja (ej., "Niño")
        self.clasificacion = clasificacion

    def __str__(self):
        # Devuelve una representación en cadena del nodo para facilitar el debugging
        return f"Nodo({self.criterio}, {self.valor}, Hoja={self.es_hoja}, Clasificación={self.clasificacion})"
