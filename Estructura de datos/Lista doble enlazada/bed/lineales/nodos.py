class NodoListaDE:
    """
     Clase que modela los nodos para una lista doble enlazada
    """
    def __init__(self, dato, siguiente=None, anterior=None):
        """
        __init__
        Inicializa un nodo con un dato.

        Parameters
        ----------
        dato : Nodo
            Recibe un dato ya sea string, bool, int, float, etc...
        siguiente: Nodo
            Referencia el siguiente nodo de la lista, de lo contrario None
        anterior: Nodo
            Referencia el anterior nodo de la lista, de lo contrario None
        """

        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

    def __str__(self):
        """
        __str__ _summary_
        Metodo para imprimir el nodo

        Returns
        -------
        STRING
            devuelve el dato en string
        """
        return str(self.dato)
