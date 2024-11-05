class DuplicatedKeyError(Exception):
    pass


class nodoArbolDecision:
    def __init__(self, clave):
        self.clave = clave  # clave es un tuple (nombre_categoria, limite_edad)
        self.izq = None
        self.der = None


class ArbolDecision:
    def __init__(self):
        self.raiz = None

    def adicionar(self, nueva_clave):
        if self.raiz is None:
            self.raiz = nodoArbolDecision(nueva_clave)
        else:
            self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):
        nombre_categoria, limite_edad = nueva_clave
        _, limite_actual = sub_arbol.clave

        if limite_edad < limite_actual:
            if sub_arbol.izq is None:
                sub_arbol.izq = nodoArbolDecision(nueva_clave)
            else:
                self.__adicionar(sub_arbol.izq, nueva_clave)
        elif limite_edad > limite_actual:
            if sub_arbol.der is None:
                sub_arbol.der = nodoArbolDecision(nueva_clave)
            else:
                self.__adicionar(sub_arbol.der, nueva_clave)
        else:
            raise DuplicatedKeyError(nueva_clave)

    def evaluar(self, edad):
        return self.__evaluar(self.raiz, edad)

    def __evaluar(self, sub_arbol, edad):
        if sub_arbol is None:
            return None

        nombre_categoria, limite_edad = sub_arbol.clave
        if edad <= limite_edad:
            return nombre_categoria
        else:
            return self.__evaluar(sub_arbol.der, edad)


# Ejemplo de uso
if __name__ == "__main__":
    arbol_decision = ArbolDecision()

    # Adicionando nodos de decisión
    arbol_decision.adicionar(("Niño", 12))
    arbol_decision.adicionar(("Adolescente", 17))
    arbol_decision.adicionar(("Adulto Joven", 25))
    arbol_decision.adicionar(("Adulto Mayor", 60))

    # Evaluando edades
    print(arbol_decision.evaluar(10))  # Niño
    print(arbol_decision.evaluar(15))  # Adolescente
    print(arbol_decision.evaluar(20))  # Adulto Joven
    print(arbol_decision.evaluar(65))  # Adulto Mayor
    print(arbol_decision.evaluar(70))  # None (no hay categoría para mayores de 60)
