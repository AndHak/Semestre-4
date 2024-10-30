class nodoArbol_Bin:

    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
    
    def tiene_hijos(self):
        return True if self.izq or self.der else False
    
    def __str__(self):
        return f"{self.clave}"
    