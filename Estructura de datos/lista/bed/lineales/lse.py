from nodos import Nodo_listaSE

class Lista_SE:
    """Clase que crea una lista simplemente enlazada."""

    def __init__(self):
        """Método constructor de un objeto de una lista simplemente enlazada."""
        self.__cab = None

    def es_vacia(self):
        """Método que retorna un dato de tipo booleano si la lista está vacía.

        Returns
        -------
        bool
            True si la lista está vacía, de lo contrario retorna False.
        """
        return self.__cab is None

    def adicionar(self, nuevo_dato):
        """Adiciona un nuevo dato al final de la lista.

        Parameters
        ----------
        nuevo_dato : any
            El dato que se desea agregar a la lista.
        """
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            actual = self.__cab
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo_nodo

    def recorrer(self):
        """Método que recorre la lista imprimiendo cada uno de los datos que contiene."""
        actual = self.__cab
        while actual:
            print(actual.dato)
            actual = actual.sig

    def encontrar(self, dato):
        """Busca un dato en la lista.

        Parameters
        ----------
        dato : any
            El dato que se desea buscar en la lista.

        Returns
        -------
        any
            El dato si es encontrado, de lo contrario None.
        """
        actual = self.__cab
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.sig
        return None

    def ordenar(self, key=None, reverse=False):
        """Ordena la lista en orden ascendente o descendente usando una clave opcional.

        Parameters
        ----------
        key : function, optional
            Una función que toma un elemento y devuelve un valor que se usa para comparar (por defecto es None, lo que significa que los elementos se comparan directamente).
        reverse : bool, optional
            Si es True, la lista se ordena en orden descendente (por defecto es False, para orden ascendente).
        """
        if self.es_vacia():
            return

        # Si no se proporciona una clave, se usa una función de identidad.
        if key is None:
            key = lambda x: x

        # Proceso de ordenación por burbuja
        ordenando = True
        while ordenando:
            ordenando = False
            actual = self.__cab
            while actual and actual.sig:
                # Se maneja la clave comparativa de manera segura
                try:
                    valor_actual = key(actual.dato)
                except TypeError:
                    valor_actual = actual.dato  # Si no es posible aplicar key, usar el dato directamente

                try:
                    valor_siguiente = key(actual.sig.dato)
                except TypeError:
                    valor_siguiente = actual.sig.dato

                if (valor_actual > valor_siguiente) if not reverse else (valor_actual < valor_siguiente):
                    actual.dato, actual.sig.dato = actual.sig.dato, actual.dato
                    ordenando = True
                actual = actual.sig

    def ordenar_descendente(self):
        """Ordena la lista en orden descendente."""
        self.ordenar(reverse=True)

    def remover(self, posicion):
        """Elimina un nodo de la lista en una posición específica.

        Parameters
        ----------
        posicion : int
            La posición del nodo a eliminar (0 para el primer nodo).

        Returns
        -------
        any
            El dato del nodo eliminado o None si la posición es inválida.
        """
        if self.es_vacia():
            return None
        
        if posicion == 0:
            dato_eliminado = self.__cab.dato
            self.__cab = self.__cab.sig
            return dato_eliminado
        
        actual = self.__cab
        indice = 0
        previo = None
        while actual and indice < posicion:
            previo = actual
            actual = actual.sig
            indice += 1

        if actual is None:
            return None

        dato_eliminado = actual.dato
        previo.sig = actual.sig
        return dato_eliminado

    def __iter__(self):
        """Hace que la lista sea iterable.

        Returns
        -------
        iterator
            Iterador sobre los datos de la lista.
        """
        actual = self.__cab
        while actual:
            yield actual.dato
            actual = actual.sig


if __name__ == "__main__":
    lista = Lista_SE()
    lista.adicionar(5)
    lista.adicionar(16)
    lista.adicionar(12)
    lista.adicionar(-23)
    lista.adicionar(1)
    lista.adicionar("hola")
    lista.adicionar("que hace?")
    lista.adicionar("a")
    
    print("Lista original:")
    lista.recorrer()

    print("\nIterando sobre la lista:")
    for item in lista:
        print(item)

    print("\nOrdenar por longitud de cadena (clave personalizada)")
    lista.ordenar(key=lambda x: len(x) if isinstance(x, str) else 0)
    lista.recorrer()
    lista.remover(5)
    print("")
    lista.recorrer()
