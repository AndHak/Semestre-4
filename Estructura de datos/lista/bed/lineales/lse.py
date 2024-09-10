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

    def adicionar (self,nuevo_dato):
        nuevo_nodo = Nodo_listaSE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo
        else:
            #caso cuando la lista no es vacia
            actual = self.__cab
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo_nodo

    def recorrer (self):
        #metodo que recorre la lista imprimiendo cada uno de los datos que contenga siempre y cuando no sa una lista vacia
        actual = self.__cab
        while actual:
            print(actual)
            actual = actual.sig

    def encontrar(self, dato):
        actual = self.__cab
        while actual:
            if actual.dato == dato:
                return actual.dato
            actual = actual.sig


    def ordenar(self):
        ordenando = True
        while ordenando:
            ordenando = False
            actual = self.__cab
            while actual and actual.sig:
                if actual.dato > actual.sig.dato:
                    actual.dato, actual.sig.dato = actual.sig.dato, actual.dato
                    ordenando = True
                actual = actual.sig

    def ordenar_descendente(self):
        ordenando = True
        while ordenando:
            ordenando = False
            actual = self.__cab
            while actual and actual.sig:
                if actual.dato < actual.sig.dato:
                    actual.dato, actual.sig.dato = actual.sig.dato, actual.dato
                    ordenando = True
                actual = actual.sig

if __name__ == "__main__":

    lista = Lista_SE()
    lista.adicionar(5)
    lista.adicionar(16)
    lista.adicionar(12)
    lista.adicionar(-23)
    lista.adicionar(1)
    lista.adicionar("k")
    lista.recorrer()
    print("Buscando 4")
    lista.encontrar(4)
    print("Buscando 5")
    lista.encontrar(5)
    print("Buscando 12")
    lista.encontrar(12)
    print("Ordenar normal")
    lista.ordenar()
    lista.recorrer()
    print("Ordenar descendente")
    lista.ordenar_descendente()
    lista.recorrer()

    
