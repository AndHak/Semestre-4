# ANDRES FELIPE MARTINEZ GUERRA
# SEBASTIAN DAVID ORDOÑEZ BOLAÑOS
from nodos import NodoListaDE

class Lista_DE:
    """
     Clase que implementa el funcionamiento de una lista doblemente enlazada
    """

    def __init__(self):
        """
        __init__         
        Método que realiza la creación e inicialización de la
        Lista Doblemente Enlazada.
        """
        self.__head = self.__tail = None
        self.__size = 0
        self.__inverso = False

    def __str__(self) -> str:
        """
        __str__
        Retorna una presentacion de los datos separados por <=>

        Returns
        -------
        str
            Retorna una cadena con los datos de la lista doble enlazada donde dato <=> dato
        """
        return " <=> ".join(map(str, (nodo.dato for nodo in self.adelante())))
        
    def __iter__(self):
        """
        Retorna un iterador para recorrer la lista en orden normal o inverso.

        Returns
        -------
        generator
            Un generador que recorre los nodos en el orden establecido.
        """
        return self.atras() if self.__inverso else self.adelante()    

    def __len__(self) -> int:
        """
        __len__ 
        Retorna el tamaño de la lista

        Returns
        -------
        int
            Numero de nodos en la lista
        """
        return self.__size

    def es_vacia(self) -> bool:
        """
        es_vacia
        Verifica si la lista esta vacia

        Returns
        -------
        bool
            True si la lista esta vacia, de lo contrario False
        """
        return self.__head is None

    def adicionar(self, nuevo_dato) -> bool:
        """
        Agrega un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            Dato que se agrega a la lista.

        Returns
        -------
        bool
            True si la operación es exitosa.
        """
        nuevo_nodo = NodoListaDE(nuevo_dato)
        if self.es_vacia():
            self.__head = self.__tail = nuevo_nodo
        else:
            self.__tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.__tail
            self.__tail = nuevo_nodo
        self.__size += 1
        return True

    def posicionar(self, nuevo_dato, pos=0) -> bool:
        """
        Inserta un nuevo nodo en una posicion específica.

        Parameters
        ----------
        nuevo_dato : object
            Dato a agregar a la lista.
        pos : int, opcional
            Posición en la que insertar el nuevo nodo, por defecto 0 (inicio).

        Returns
        -------
        bool
            True si la operación es exitosa.
        """
        if pos < 0 or pos > self.__size:
            return False
        if pos == 0:
            return self.__insertar_inicio(nuevo_dato)
        elif pos == self.__size:
            return self.adicionar(nuevo_dato)
        else:
            return self.__insertar_medio(nuevo_dato, pos)

    def __insertar_inicio(self, nuevo_dato):
        """
        Inserta un nuevo nodo al inicio de la lista.

        Parameters
        ----------
        nuevo_dato : object
            Dato a agregar al inicio de la lista.

        Returns
        -------
        bool
            True si la operación es exitosa.
        """
        nuevo_nodo = NodoListaDE(nuevo_dato, siguiente=self.__head)
        if self.es_vacia():
            self.__head = self.__tail = nuevo_nodo
        else:
            self.__head.anterior = nuevo_nodo
            self.__head = nuevo_nodo
        self.__size += 1
        return True

    def __insertar_medio(self, nuevo_dato, pos):
        """
        Inserta un nuevo nodo en una posición intermedia.

        Parameters
        ----------
        nuevo_dato : object
            Dato a agregar en la posición intermedia.
        pos : int
            Posición en la que insertar el nuevo nodo.

        Returns
        -------
        bool
            True si la operación es exitosa.
        """
        nodo_actual = self.ubicar(pos - 1)
        nuevo_nodo = NodoListaDE(nuevo_dato, siguiente=nodo_actual, anterior=nodo_actual.anterior)
        if nodo_actual.anterior:
            nodo_actual.anterior.siguiente = nuevo_nodo
        else:
            self.__head = nuevo_nodo
        nodo_actual.anterior = nuevo_nodo
        self.__size += 1
        return True

    def remover(self, item, por_pos=True) -> bool:
        """
        Elimina un nodo por dato o posición.

        Parameters
        ----------
        item : object o int
            Dato del nodo a eliminar o la posición del nodo a eliminar.
        por_pos : bool, opcional
            Indica si se elimina por posición (True) o por dato (False), por defecto True.

        Returns
        -------
        bool
            True si la operación es exitosa, False en caso contrario.
        """
        if por_pos and (item < 0 or item >= self.__size): 
            return False
        nodo_actual = self.ubicar(item) if por_pos else self.encontrar(item)
        if nodo_actual:
            return self.__remove_node(nodo_actual)
        return False

    def __remove_node(self, nodo):
        """
        Elimina el nodo de la lista.

        Parameters
        ----------
        nodo : NodoListaDE
            Nodo a eliminar.

        Returns
        -------
        bool
            True si la operación es exitosa.
        """
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.__head = nodo.siguiente  

        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.__tail = nodo.anterior 

        self.__size -= 1
        return True

    def encontrar(self, dato_buscar) -> object:
        """
        Busca un nodo por su dato.

        Parameters
        ----------
        dato_buscar : object
            Dato del nodo a buscar.

        Returns
        -------
        NodoListaDE o None
            El nodo que contiene el dato, None si no esta.
        """
        for nodo in self.adelante():
            if nodo.dato == dato_buscar:
                return nodo
        return None

    def ubicar(self, pos) -> object:
        """
        Obtiene el nodo en una posición específica.

        Parameters
        ----------
        pos : int
            Posición del nodo a obtener.

        Returns
        -------
        NodoListaDE o None
            El nodo en la posición especificada, None si no esta.
        """
        if 0 <= pos < self.__size:
            nodo_actual = self.__head
            for i in range(pos):
                nodo_actual = nodo_actual.siguiente
            return nodo_actual 
        return None

    def adelante(self):
        """
        Generador para recorrer la lista hacia adelante.

        Yields
        ------
        NodoListaDE
            Los nodos de la lista en orden hacia adelante.
        """
        nodo_actual = self.__head
        while nodo_actual:
            yield nodo_actual
            nodo_actual = nodo_actual.siguiente

    def atras(self):
        """
        Generador para recorrer la lista hacia atrás.

        Yields
        ------
        NodoListaDE
            Los nodos de la lista en orden inverso.
        """
        nodo_actual = self.__tail
        while nodo_actual:
            yield nodo_actual
            nodo_actual = nodo_actual.anterior

    @property
    def inverso(self) -> bool:
        """
        Propiedad que indica si la lista se recorre en orden inverso.

        Returns
        -------
        bool
            True si la lista se recorre en orden inverso, False caso contrario.
        """
        return self.__inverso

    @inverso.setter
    def inverso(self, valor: bool):
        """
        Establece si la lista se recorre en orden inverso.

        Parameters
        ----------
        valor : bool
            Nuevo valor para el modo inverso.
        """
        self.__inverso = valor

