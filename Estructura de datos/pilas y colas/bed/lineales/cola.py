# ANDRES FELIPE MARTINEZ GUERRA
# SEBASTIAN DAVID ORDOÑEZ BOLAÑOS 
from nodos import Nodo_listaSE

class Cola:
    """Clase que implementa el funcionamiento del TAD Cola
    """
    def __init__(self):
        """Método que realiza la creación e inicialización de la Cola
        """
        self.__frente = None
        self.__tam = 0
        #self.__tipodato = tipodato
    
    def es_vacia(self):
        """Método que verifica si la cola se encuentra vacía
        Returns
        -------
        bool
        Retorna True si la cola es vacia. False en caso contrario
        """
        return self.__frente is None
    
    def encolar(self, nuevo_dato):
        """Método que adiciona un nuevo dato al final de la cola. Realizar la
        validación de Homogeneidad para cada dato ingresado a la cola
        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la cola
        Returns
        -------
        bool
        True si nuevo_dato fue encolado. False en caso contrario
        """
        if self.__frente and not isinstance(nuevo_dato, type(self.__frente.dato)):
            return False
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if self.__frente:
            actual = self.__frente
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo_nodo
        else:
            self.__frente = nuevo_nodo
        self.__tam += 1  
        return True
    
    def desencolar(self):
        """Método que saca/quita el primer nodo (elimina el nodo) de la cola
        y retorna su dato
        Returns
        -------
        object|None
        El dato del primer nodo de la cola y None cuando la cola no
        contenga nodos/datos
        """
        if self.__frente:
            actual = self.__frente.dato
            self.__frente = self.__frente.sig
            self.__tam -= 1
            return actual
        return None
    
    def frente(self):
        """Método que retorna el dato del primer nodo de la cola, sin quitarlo
        de la misma
        Returns
        -------
        object|None
        El dato del primer nodo en la cola y None cuando la cola no
        contenga nodos/datos"""
        return self.__frente.dato if self.__frente else None
    
    def __len__(self):
        """Método que retorna del número de nodos que contiene la cola
        Returns
        -------
        int
        Tamaño de la cola
        """
        return self.__tam

    def __iter__(self):
        actual = self.__frente
        while actual:
            yield actual
            actual = actual.sig

    
    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la cola
        Returns
        -------
        str
        Una cadena que muestre todos los datos que actualmente almacena
        la cola, en el siguiente formato:
        “@|<-{dato }<-[dato ]<-[dato ]<-[dato_n]”₁ ₂ ₃
        Cuando hay un sólo dato:
        “@|<-{dato }”₁
        Cuando no hay datos:
        “@|”
        """
        if self.es_vacia():
            return "@|"
        nodos = [f"{{{nodo.dato}}}" if nodo == self.__frente else f"[{nodo.dato}]" for nodo in self]
        return "@|<-" + "<-".join(nodos)