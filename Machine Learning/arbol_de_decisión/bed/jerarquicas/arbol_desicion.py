from bed.jerarquicas.excepciones import DuplicatedKeyError, HomogeneityError
from bed.jerarquicas.nodos import *
from bed.jerarquicas.arbol_desicion import ArbolDecision

class ArbolDecision:
    def __init__(self):
        self.raiz = None

    def adicionar(self, pregunta, resultado=None):
        """Método que permite agregar un nuevo nodo de decisión al árbol."""
        self.raiz = self.__adicionar(self.raiz, pregunta, resultado)

    def __adicionar(self, sub_arbol, pregunta, resultado):
        if sub_arbol is None:
            return NodoDecision(pregunta=pregunta, resultado=resultado)
        
        if pregunta < sub_arbol.pregunta:
            sub_arbol.izquierdo = self.__adicionar(sub_arbol.izquierdo, pregunta, resultado)
        else:
            sub_arbol.derecho = self.__adicionar(sub_arbol.derecho, pregunta, resultado)

        return sub_arbol

    def encontrar(self, pregunta_buscar):
        """Método que realiza la búsqueda de una pregunta en el árbol de decisión."""
        return self.__encontrar(self.raiz, pregunta_buscar)

    def __encontrar(self, sub_arbol, pregunta_buscar):
        if sub_arbol is None:
            return None
        if sub_arbol.pregunta == pregunta_buscar:
            return sub_arbol.resultado
        elif pregunta_buscar < sub_arbol.pregunta:
            return self.__encontrar(sub_arbol.izquierdo, pregunta_buscar)
        else:
            return self.__encontrar(sub_arbol.derecho, pregunta_buscar)

    def encontrar_minimo(self):
        """Método que busca y retorna la pregunta con menor valor."""
        if not self.raiz:
            return None
        return self.__encontrar_minimo(self.raiz)

    def __encontrar_minimo(self, sub_arbol):
        if sub_arbol.izquierdo:
            return self.__encontrar_minimo(sub_arbol.izquierdo)
        return sub_arbol.pregunta

    def encontrar_maximo(self):
        """Método que busca y retorna la pregunta con mayor valor."""
        if not self.raiz:
            return None
        return self.__encontrar_maximo(self.raiz)

    def __encontrar_maximo(self, sub_arbol):
        if sub_arbol.derecho:
            return self.__encontrar_maximo(sub_arbol.derecho)
        return sub_arbol.pregunta

    def eliminar(self, pregunta_eliminar):
        """Método que elimina un nodo del árbol de decisión."""
        self.raiz = self.__eliminar(self.raiz, pregunta_eliminar)

    def __eliminar(self, sub_arbol, pregunta_eliminar):
        if sub_arbol is None:
            return sub_arbol

        if pregunta_eliminar < sub_arbol.pregunta:
            sub_arbol.izquierdo = self.__eliminar(sub_arbol.izquierdo, pregunta_eliminar)
        elif pregunta_eliminar > sub_arbol.pregunta:
            sub_arbol.derecho = self.__eliminar(sub_arbol.derecho, pregunta_eliminar)
        else:
            # Caso 1: Nodo con un solo hijo o sin hijos
            if sub_arbol.izquierdo is None:
                return sub_arbol.derecho
            elif sub_arbol.derecho is None:
                return sub_arbol.izquierdo

            # Caso 2: Nodo con dos hijos
            temp = self.__encontrar_minimo(sub_arbol.derecho)
            sub_arbol.pregunta = temp
            sub_arbol.derecho = self.__eliminar(sub_arbol.derecho, temp)

        return sub_arbol

    def __str__(self):
        return self.__str_recursivo(self.raiz)

    def __str_recursivo(self, sub_arbol):
        if sub_arbol is None:
            return ""
        return f"{self.__str_recursivo(sub_arbol.izquierdo)}{sub_arbol.pregunta}\n{self.__str_recursivo(sub_arbol.derecho)}"
