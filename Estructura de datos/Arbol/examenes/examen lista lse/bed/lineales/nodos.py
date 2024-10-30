class Nodo_listaSE:
    """clase que modela un nodo para el tipo de estructura lista simplemete 
    enlazada.
    """
    def __init__(self,dato):
        """Metodo constructor de un nodo para una lista simplemente enlazada

        Parameters
        ----------
        dato : object
            El dato que se pasa al nodo
        """
        
        self.dato = dato
        self.sig = None
    
    def __str__(self):
        """Metodo que retorna una cadena con el dato del nodo                       
        Returns
        -------
        str
            la cadena a ser retornada por el nodo, que incluye el dato
        """
        return f"{self.dato}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# if __name__ == "__main__":
#     nodo1 = Nodo_listaSE(8)
#     nodo2 = Nodo_listaSE(5)
#     nodo3 = Nodo_listaSE(10)
#     nodo4 = Nodo_listaSE(2)
#     nodo1.sig = nodo2
#     nodo2.sig = nodo3
#     nodo3.sig = nodo4
    

#     aux=nodo1
#     while aux != None:
#         print (aux)
#         aux=aux.sig
    