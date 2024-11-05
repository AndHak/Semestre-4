# MÉTODOS DE RECORRIDO
def pre_orden(self):
    self.__pre_orden(self.raiz)

def __pre_orden(self, sub_arbol):
    if sub_arbol:
        print(sub_arbol.pregunta, end=" ")
        self.__pre_orden(sub_arbol.izquierdo)
        self.__pre_orden(sub_arbol.derecho)

def str_pre_orden(self, sep="|"):
    resultado = []
    self.__str_pre_orden(self.raiz, resultado, sep, True)
    return sep.join(resultado)

def __str_pre_orden(self, sub_arbol, resultado, sep, es_raiz):
    if sub_arbol:
        tipo_nodo = "[🌲]{}" if es_raiz else "(🌿){}"
        if sub_arbol.izquierdo is None and sub_arbol.derecho is None:
            tipo_nodo = "(🍂){}"  # Nodo hoja
        resultado.append(tipo_nodo.format(sub_arbol.pregunta))
        self.__str_pre_orden(sub_arbol.izquierdo, resultado, sep, False)
        self.__str_pre_orden(sub_arbol.derecho, resultado, sep, False)

def in_orden(self):
    self.__in_orden(self.raiz)

def __in_orden(self, sub_arbol):
    if sub_arbol:
        self.__in_orden(sub_arbol.izquierdo)
        print(sub_arbol.pregunta, end=" ")  # Imprime la pregunta
        self.__in_orden(sub_arbol.derecho)

def str_in_orden(self, sep=":"):
    resultado = []
    self.__str_in_orden(self.raiz, resultado, sep, True)
    return sep.join(resultado)

def __str_in_orden(self, sub_arbol, resultado, sep, es_raiz):
    if sub_arbol:
        self.__str_in_orden(sub_arbol.izquierdo, resultado, sep, False)
        tipo_nodo = "[🌲]{}" if es_raiz else "(🌿){}"
        if sub_arbol.izquierdo is None and sub_arbol.derecho is None:
            tipo_nodo = "(🍂){}"  # Nodo hoja
        resultado.append(tipo_nodo.format(sub_arbol.pregunta))
        self.__str_in_orden(sub_arbol.derecho, resultado, sep, False)

def post_orden(self):
    self.__post_orden(self.raiz)

def __post_orden(self, sub_arbol):
    if sub_arbol:
        self.__post_orden(sub_arbol.izquierdo)
        self.__post_orden(sub_arbol.derecho)
        print(sub_arbol.pregunta, end=" ")  # Imprime la pregunta

def str_post_orden(self, sep="^"):
    resultado = []
    self.__str_post_orden(self.raiz, resultado, sep, True)
    return sep.join(resultado)

def __str_post_orden(self, sub_arbol, resultado, sep, es_raiz):
    if sub_arbol:
        self.__str_post_orden(sub_arbol.izquierdo, resultado, sep, False)
        self.__str_post_orden(sub_arbol.derecho, resultado, sep, False)
        tipo_nodo = "[🌲]{}" if es_raiz else "(🌿){}"
        if sub_arbol.izquierdo is None and sub_arbol.derecho is None:
            tipo_nodo = "(🍂){}"  # Nodo hoja
        resultado.append(tipo_nodo.format(sub_arbol.pregunta))