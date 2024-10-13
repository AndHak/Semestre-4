class Nodo_listaSE:
    """Clase que modela un nodo para el tipo de estructura enlazada
    """
    
    def __init__(self, dato):
        """metodo contructor de un nodo para una lista simplemente enlazada

        Parameters
        ----------
        dato : object
            el dato que se pasa al nodo
        """
        self.dato = dato
        self.sig = None
    
    def __str__(self):
        """metodo que retorna una cadena con el dato del nodo

        Returns
        -------
        str
            la cadena a ser retornada por el nodo que incluye el dato
        """
        return str(self.dato)

