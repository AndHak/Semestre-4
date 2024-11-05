class NodoDecision:
    def __init__(self, pregunta=None, izquierdo=None, derecho=None, resultado=None):
        self.pregunta = pregunta  # Pregunta que divide el árbol
        self.izquierdo = izquierdo  # Subárbol izquierdo
        self.derecho = derecho      # Subárbol derecho
        self.resultado = resultado  # Resultado en caso de ser una hoja

    def __str__(self):
        return f"Pregunta: {self.pregunta}, Resultado: {self.resultado}"

class nodoArbol_Decision:
    def __init__(self, clave, valor=None, es_hoja=False):
        self.clave = clave
        self.valor = valor
        self.es_hoja = es_hoja
        self.izq = None
        self.der = None

    def __str__(self):
        return f"Clave: {self.clave}, Valor: {self.valor}, Es hoja: {self.es_hoja}"

class nodoArbol_Bin:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
    
    def tiene_hijos(self):
        return True if self.izq or self.der else False
    
    def __str__(self):
        return f"{self.clave}"
