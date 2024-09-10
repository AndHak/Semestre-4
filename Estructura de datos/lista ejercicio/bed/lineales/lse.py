from nodos import Nodo_listaSE

class Lista_SE:
    """Clase qie crea una lista simplemente enlazada
    """

    def __init__(self):
        """metodo contructor de un objeto de una lista simplemente enlazada
        """
        
        #este atributo va a quedar oculto con __
        self.__cab = None
    
    def es_vacia(self):
        """metodo que retorna un dato de tipo booleano si la lista esta vacia

        Returns
        -------
        bool
            True si la lista esta vacia de lo contrario retorna False
        """

        if not self.__cab:
            return True
        return False