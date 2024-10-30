from bed.jerarquicas.nodos import nodoArbol_Bin
from random import random

class arbolBin:

    def __init__(self):
        self.raiz = None

    def adicionar(self, nueva_clave):
        self.raiz = self.__adicionar(self.raiz, nueva_clave)
    
    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = nodoArbol_Bin(nueva_clave)
        elif random() <= 0.5: #adicionar por izq
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        else:
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)

        return sub_arbol

    def encontrar(self, clave_encontrar):
        return self.__encontrar(self.raiz, clave_encontrar)
    
    def __encontrar(self, sub_arbol, clave_encontrar):
        if sub_arbol:
            print(sub_arbol.clave, "<-->", clave_encontrar)
            print(("O" if sub_arbol.izq else "X") + ":" + 
                  ("O" if sub_arbol.der else "X"))
            if sub_arbol.clave == clave_encontrar:
                return sub_arbol.clave
            else:
                clave_izq = self.__encontrar(sub_arbol.izq, clave_encontrar)
                if clave_izq == clave_encontrar:
                    return clave_izq
                clave_der = self.__encontrar(sub_arbol.der, clave_encontrar)
                if clave_der == clave_encontrar:
                    return clave_der
        return None

    def __len__(self):
        return self.__cantidad_nodos(self.raiz)
    
    def __cantidad_nodos(self, sub_arbol):
        if sub_arbol:
            return (1 + self.__cantidad_nodos(sub_arbol.izq) + self.__cantidad_nodos(sub_arbol.der))
        else:
            return 0
        
    def hojas(self):
            """Cuenta el número de nodos hoja en el árbol."""
            return self.__hojas(self.raiz)

    def __hojas(self, sub_arbol):
        if sub_arbol is None:
            return 0
        if sub_arbol.izq is None and sub_arbol.der is None:
            return 1  # Nodo hoja
        return self.__hojas(sub_arbol.izq) + self.__hojas(sub_arbol.der)

    def internos(self):
        """Cuenta el número de nodos internos en el árbol."""
        return self.__internos(self.raiz)

    def __internos(self, sub_arbol):
        if sub_arbol is None or (sub_arbol.izq is None and sub_arbol.der is None):
            return 0
        return 1 + self.__internos(sub_arbol.izq) + self.__internos(sub_arbol.der)

    def altura(self):
        """Calcula la altura del árbol binario."""
        return self.__altura(self.raiz)

    def __altura(self, sub_arbol):
        if sub_arbol is None:
            return 0
        return 1 + max(self.__altura(sub_arbol.izq), self.__altura(sub_arbol.der))

    





