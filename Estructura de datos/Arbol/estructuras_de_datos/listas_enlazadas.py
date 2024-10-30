#listas simplemente enlazadas
class Nodo_listaSE:

    def __init__(self, dato):
        self.dato = dato
        self.sig = None
    
    def __str__(self):
        return str(self.dato)
    
        
    # def agregar_sig(dato):
    #     nuevo_nodo = Nodo_listaSE(dato)
    #     if nuevo_nodo == None:
    #         nuevo_nodo = self.dato
    #     else:
    #         while nuevo_nodo =! None:
                

    
if __name__ == "__main__":
    
    nodo1 = Nodo_listaSE(8)
    nodo2 = Nodo_listaSE(5)
    nodo3 = Nodo_listaSE(10)
    nodo4 = Nodo_listaSE(2)


    nodo1.sig = nodo2
    nodo2.sig = nodo3
    nodo3.sig = nodo4

    nodo_actual = nodo1
    while nodo_actual != None:
        print(nodo_actual)
        nodo_actual = nodo_actual.sig

    
