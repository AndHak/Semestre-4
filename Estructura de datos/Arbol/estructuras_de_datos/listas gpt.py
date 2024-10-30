class Nodo_listaSE:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

    def __str__(self):
        return str(self.dato)

class ListaSE:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo_listaSE(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.sig is not None:
                nodo_actual = nodo_actual.sig
            nodo_actual.sig = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual, end=" -> ")
            nodo_actual = nodo_actual.sig
        print("None")
