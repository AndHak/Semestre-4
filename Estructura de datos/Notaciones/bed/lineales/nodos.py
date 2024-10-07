
class Nodo_listaSE:
    """Clase que implementa el funcionamiento de un nodo para la estructura Lista Simplemente Enlazada
    """
    def __init__(self, dato):
        """Método que permite construir un objeto de tipo Nodo de una LSE.

        Parameters
        ----------
        dato : object
            El dato a ser pasado al nodo.
        """
        self.dato = dato
        self.sig = None

    def __str__(self):
        """Método que devuelve una cadena con el dato del nodo.

        Returns
        -------
        str
            La cadena del dato a ser retornado.
        """
        return f"{self.dato}"
    
class Nodo_listaCSE(Nodo_listaSE):
    """Clase que implementa el funcionamiento de un nodo para la estructura Lista Circular Simplemente Enlazada
    

    Parameters
    ----------
    Nodo_listaSE : object
        clase padre de la clase Nodo_listaCSE
    """
    def __init__(self, dato):
        """Método que permite construir un objeto de tipo Nodo de una LCSE.

        Parameters
        ----------
        dato : object
            El dato a ser pasado al nodo.
        """
        super().__init__(dato)