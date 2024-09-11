from nodos import Nodo_listaSE

class Lista_SE:
    """Clase que implementa el funcionamiento de una lista simplemente enlazada"""

    # (1) Método Constructor
    def __init__(self):
        """Método que realiza la creación e inicialización de la
        Lista Simplemente Enlazada.
        """
        self.__cab = None        

    # (2) Método es_vacia
    def es_vacia(self):
        """Método que verifica si la lista se encuentra vacía.

        Returns
        -------
        bool
            Retorna True si la lista es vacia. False en caso contrario.
        """
        return self.__cab is None

    # (3.1) Método adicionar al final de la lista
    def adicionar(self, nuevo_dato):
        """ Método que adiciona un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.

        Returns
        -------
        bool
            True cuando el dato es añadido en la lista. False en caso
            contrario.
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            actual = self.__cab
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo_nodo
        return True
       
    # (3.2) Método posicionar
    def posicionar(self, nuevo_dato, pos):
        """Método que inserta un nuevo nodo en cualquier posición de la
        lista. Si la lista está vacía la única posición válida será
        cero. Si la lista ya contiene datos, serán válidas posiciones
        intermedias o la posición inmediatemente superior a la del último dato.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser añadido a la lista.
        pos : int, optional
            Posición a insertar en la lista, por defecto 0.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista. False en caso
            contrario.
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if pos == 0:
            nuevo_nodo.sig = self.__cab
            self.__cab = nuevo_nodo
        else:
            actual = self.__cab
            indice = 0
            while actual and indice < pos - 1:
                actual = actual.sig
                indice += 1
            if actual:
                nuevo_nodo.sig = actual.sig
                actual.sig = nuevo_nodo
            else:
                return False
        return True

    # (4) Método recorrer una lista
    def recorrer(self):
        """Método que recorre la lista, imprimiendo cada uno de los datos que
        contenga, siempre y cuando no sea una lista vacía.
        """
        nodo_actual = self.__cab
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.sig

    # (5.1) Método econtrar un dato en la lista por dato
    def encontrar(self, dato_buscar):
        """Método que realiza la búsqueda de un dato en la lista.

        Parameters
        ----------
        dato_buscar : object
            Corresponde al valor del dato a ser encontrado en la lista.

        Returns
        -------
        object|None
            object si se encuentra el dato en la lista, None en caso contrario.
        """
        actual = self.__cab
        while actual:
            if actual.dato == dato_buscar:
                return actual
            actual = actual.sig
        return None

    # (5.2) Método ubicar un dato por posición en la lista
    def ubicar(self, pos):
        """Método que realiza la búsqueda de un dato en la lista dependiendo
        de la posición ingresada.

        Parameters
        ----------
        pos : int
            Corresponde a la posición en la lista a ubicar el dato.

        Returns
        -------
        object|None
            object si el dato es ubicado en la lista, None en caso contrario.
        """
        if pos >= 0:
            actual = self.__cab
            indice = 0
            while actual and indice < pos:
                actual = actual.sig
                indice += 1
            if actual and indice == pos:
                return actual.dato
        return None
    
    # (6) Método remover por dato (* CONSULTA) o posición
    def remover(self, item, por_pos=True):
        """Método que permite remover un nodo de la lista ya sea por una
        posición o por el dato correspondiente. Si es por dato, deberá
        remover cada uno de los nodos que contenga dicho dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder al valor del dato a ser removido de la lista
            o a la posición en la lista a remover el dato.
            En el caso de remover por dato, se buscará todas las coincidencias
            del dato a eliminar en la lista y serán quitadas.
        por_pos : bool, optional
            Si es True, el método intentará remover un dato por su posición,
            de lo contrario se intentará hacerlo por su valor, por defecto True.

        Returns
        -------
        bool
            True cuando el dato es removido de la lista. False en caso
            contrario.
        """
        if por_pos:
            return self.__remover_pos(item)
        else:
            # CONSULTA: remover por dato
            return self.__remover_dato(item)
    
    # (6.1) Método oculto remover por posición
    def __remover_pos(self, pos_elim):
        actual = self.__cab
        indice = 0 
        anterior = None

        if pos_elim >= 0:
            while actual and indice < pos_elim:
                anterior = actual
                actual = actual.sig
                indice+= 1

            if indice == 0 and actual:
                self.__cab = actual.sig
            elif actual:
                anterior.sig = actual.sig
            
        return True if actual and pos_elim == indice else False
    
    """
    def __remover_pos(self, pos_elim):
        if pos_elim < 0:
            return False
        actual = self.__cab
        indice = 0 
        anterior = None

        while actual and indice < pos_elim:
            anterior = actual
            actual = actual.sig
            indice += 1

        if indice == 0 and actual:
            self.__cab = actual.sig
        elif actual:
            anterior.sig = actual.sig
        else:
            return False 
            
        return True
    """


    # (6.2) Método oculto remover por dato
    def __remover_dato(self, dato_eliminar):
        """Método que remueve todos los nodos que contengan el dato especificado.

        Parameters
        ----------
        dato_eliminar : object
            Corresponde al valor del dato a ser removido de la lista.

        Returns
        -------
        bool
            True si se eliminó al menos un nodo con el dato especificado, False en caso contrario.
        """
        eliminado = False
        anterior = None
        actual = self.__cab
        while actual:
            if actual.dato == dato_eliminar:
                if anterior:
                    anterior.sig = actual.sig
                else:
                    self.__cab = actual.sig
                eliminado = True
            else:
                anterior = actual
            actual = actual.sig
        return eliminado

    # (7) Método __str__
    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista, o una
        cadena vacía en el caso de que la lista sea vacía.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el formato:
                "(dato_0) :>: (dato_1) :>: (dato_2) :>: ... :>: (dato_n)"
                "(7) :>: (8) :>: (5) :>: (5) :>: (9)"
            de lo contrario retornará una cadena vacía: ""
        """
        if self.es_vacia():
            return ""
        else:
            actual = self.__cab
            cadena = str(actual.dato)
            while actual.sig:
                actual = actual.sig
                cadena += " :>: " + str(actual.dato)
            return cadena

    # (8) Sobre-escritura del método __len__
    def __len__(self):
        """Método que calcula el tamaño de la lista.

        Returns
        -------
        int
            El número de nodos que tiene la lista.
        """
        actual = self.__cab
        contador = 0
        while actual:
            contador += 1
            actual = actual.sig
        return contador

    # (9) Método __iter__
    def __iter__(self):
        """Método que permite iterar sobre los elementos de la lista.

        Yields
        ------
        object
            Cada uno de los datos almacenados en los nodos de la lista.
        """
        actual = self.__cab
        while actual:
            yield actual.dato
            actual = actual.sig


if __name__ == "__main__":
    # Crear una lista simplemente enlazada
    list_num = Lista_SE()

    # Prueba 1: Adicionar nodos
    print("Prueba 1: Adicionar nodos")
    list_num.adicionar(7)
    list_num.adicionar(8)
    list_num.adicionar(10)
    list_num.recorrer()  # Esperado: 7 8 10
    print(f"Longitud de la lista: {len(list_num)}")  # Esperado: 3
    print()

    # Prueba 2: Insertar en una posición específica
    print("Prueba 2: Insertar en una posición específica")
    list_num.posicionar(9, 1)  # Inserta 9 en la posición 1
    list_num.recorrer()  # Esperado: 7 9 8 10
    print()

    # Prueba 3: Buscar un dato existente
    print("Prueba 3: Buscar un dato existente")
    encontrado = list_num.encontrar(9)
    print(f"Encontrado: {encontrado}")  # Esperado: 9
    print()

    # Prueba 4: Buscar un dato inexistente
    print("Prueba 4: Buscar un dato inexistente")
    encontrado = list_num.encontrar(100)
    print(f"Encontrado: {encontrado}")  # Esperado: None
    print()

    # Prueba 5: Remover por posición
    print("Prueba 5: Remover por posición")
    list_num.remover(2, por_pos=True)  # Elimina el nodo en la posición 2 (8)
    list_num.recorrer()  # Esperado: 7 9 10
    print()

    # Prueba 6: Remover por dato
    print("Prueba 6: Remover por dato")
    list_num.remover(9, por_pos=False)  # Elimina el nodo con el dato 9
    list_num.recorrer()  # Esperado: 7 10
    print()

    # Prueba 7: Insertar en la primera posición
    print("Prueba 7: Insertar en la primera posición")
    list_num.posicionar(5, 0)  # Inserta 5 en la primera posición
    list_num.recorrer()  # Esperado: 5 7 10
    print()

    # Prueba 8: Insertar en una posición fuera de rango
    print("Prueba 8: Insertar en una posición fuera de rango")
    exito = list_num.posicionar(99, 10)  # Intentar insertar en una posición inválida
    print(f"¿Inserción exitosa?: {exito}")  # Esperado: False
    list_num.recorrer()  # Esperado: 5 7 10
    print()

    # Prueba 9: Verificar longitud de la lista
    print("Prueba 9: Verificar longitud de la lista")
    print(f"Longitud de la lista: {len(list_num)}")  # Esperado: 3
    print()

    # Prueba 10: Probar la representación en cadena (__str__)
    print("Prueba 10: Probar la representación en cadena")
    print(str(list_num))  # Esperado: "(5) :>: (7) :>: (10)"
    print()

    # Prueba 11: Probar la iteración
    print("Prueba 11: Probar la iteración")
    for dato in list_num:
        print(f"Dato iterado: {dato}")  # Esperado: 5 7 10
    print()

    # Prueba 12: Remover por posición fuera de rango
    print("Prueba 12: Remover por posición fuera de rango")
    exito = list_num.remover(10, por_pos=True)  # Intentar remover en una posición inválida
    print(f"¿Eliminación exitosa?: {exito}")  # Esperado: False
    list_num.recorrer()  # Esperado: 5 7 10
    print()

    # Prueba 13: Remover todos los elementos
    print("Prueba 13: Remover todos los elementos")
    list_num.remover(5, por_pos=False)  # Remover 5
    list_num.remover(7, por_pos=False)  # Remover 7
    list_num.remover(10, por_pos=False)  # Remover 10
    list_num.recorrer()  # Esperado: (lista vacía)
    print(f"Lista vacía: {list_num.es_vacia()}")  # Esperado: True
