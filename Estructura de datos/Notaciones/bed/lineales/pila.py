
from nodos import Nodo_listaSE


class Pila:
    """Clase que implementa el funcionamiento del TAD Pila
    """
    def __init__(self):
        """Método constructor que realiza la creación e inicialización de
        una Pila
        """
        self.__cima: Nodo_listaSE = None
        
    def es_vacia(self):
        """Método que verifica si la pila se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la pila es vacia. False en caso contrario
        """
        return self.__cima is None
    
    def apilar(self, nuevo_dato):
        """Método que realiza la entrada de un nuevo dato a la pila.
        Realizar la validación de Homogeneidad para cada dato ingresado
        a la pila
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la pila
        Returns
        -------
        bool
        True si nuevo_dato fue apilado. False en caso contrario
        """
        if self.__cima and not isinstance(nuevo_dato, type(self.__cima.dato)):
            return False
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        nuevo_nodo.sig = self.__cima
        self.__cima = nuevo_nodo
        return True
    
    def desapilar(self):
        """Método que saca/quita el último nodo (elimina el nodo) de la pila
        y retorna su dato
        Returns
        -------
        object|None
        El dato del nodo desapilado y None cuando la pila no contenga
        nodos/datos
        """
        if self.__cima:
            dato = self.__cima.dato
            self.__cima = self.__cima.sig
            return dato
        return None
    
    def cima(self):
        """Método que retorna el dato del último nodo ingresado en la pila,
        sin quitarlo de la misma
        Returns
        -------
        object|None
        El dato del último nodo ingresado y None cuando la pila no
        contenga nodos/datos
        """
        return self.__cima.dato if self.__cima else None
    
    def __len__(self):
        """Método que retorna el número de nodos que contiene la pila
        Returns
        -------
        int
        Tamaño de la pila
        """
        actual = self.__cima
        cantidad_nodos = 0
        while actual:
            cantidad_nodos += 1
            actual = actual.sig
        return cantidad_nodos
    
    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la pila (sin desapilarlos)
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la pila, en el siguiente formato:
        “===(c)===
        (*[dato_n]*)
        ::
        (dato )₃
        ::
        (dato )₂
        ::
        (dato )”₁
        Cuando hay un sólo dato:
        “===(c)===
        (*[dato_n]*)”
        Cuando no hay datos:
        “===(c)===”
        """
        actual = self.__cima
        if actual:
            cadena_salida = "===(c)===\n"
            while actual:
                if actual is self.__cima:
                    cadena_salida += f"(*[{actual.dato}]*){'\n::\n' if actual.sig else ''}"
                else:
                    cadena_salida += f"({actual.dato}){'\n::\n' if actual.sig else ''}"
                actual = actual.sig
            return cadena_salida
        return "===(c)==="     
