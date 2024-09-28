import numpy as np
from nodos import NodoListaDE

class ListaDE:
    """
    Lista doblemente enlazada.

    Atributos
    ----------
    __head : NodoListaDE, opcional
        Referencia al primer nodo de la lista, por defecto None.
    __tail : NodoListaDE, opcional
        Referencia al último nodo de la lista, por defecto None.
    __size : int
        Tamaño de la lista, por defecto 0.
    __inverso : bool
        Indica si la lista se recorre en orden inverso, por defecto False.

    Métodos
    -------
    __init__()
        Inicializa la lista vacía.
    __str__()
        Retorna la representación en cadena de la lista.
    __len__()
        Retorna el tamaño de la lista.
    __iter__()
        Retorna un iterador para recorrer la lista en orden normal o inverso.
    es_vacia()
        Verifica si la lista está vacía.
    adicionar(nuevo_dato)
        Agrega un nuevo nodo al final de la lista.
    posicionar(nuevo_dato, pos=0)
        Inserta un nuevo nodo en una posición específica.
    remover(item, por_pos=True)
        Elimina un nodo por dato o posición.
    encontrar(dato_buscar)
        Busca un nodo por su dato.
    ubicar(pos)
        Obtiene el nodo en una posición específica.
    adelante()
        Generador para recorrer la lista hacia adelante.
    atras()
        Generador para recorrer la lista hacia atrás.
    inverso()
        Propiedad para obtener o establecer el modo inverso de la lista.
    """

    def __init__(self):
        """
        Inicializa la lista doblemente enlazada vacía.
        """
        self.__head = self.__tail = None
        self.__size = 0
        self.__inverso = False

    def __str__(self) -> str:
        """
        Retorna una representación en cadena de la lista.

        Returns
        -------
        str
            Una cadena con los datos de la lista enlazada separados por " <=> ".
        """
        return " <=> ".join(map(str, (nodo.dato for nodo in self.adelante())))

    def __len__(self) -> int:
        """
        Retorna el tamaño de la lista.

        Returns
        -------
        int
            Número de nodos en la lista.
        """
        return self.__size

    def __iter__(self):
        """
        Retorna un iterador para recorrer la lista en orden normal o inverso.

        Returns
        -------
        generator
            Un generador que recorre los nodos en el orden establecido.
        """
        return self.atras() if self.__inverso else self.adelante()

    def es_vacia(self) -> bool:
        """
        Verifica si la lista está vacía.

        Returns
        -------
        bool
            True si la lista está vacía, False en caso contrario.
        """
        return self.__head is None

    def adicionar(self, nuevo_dato) -> bool:
        """
        Agrega un nuevo nodo al final de la lista.

        Parameters
        ----------
        nuevo_dato : object
            Dato a agregar a la lista.

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
        Inserta un nuevo nodo en una posición específica.

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
        if pos <= 0:
            return self.__insertar_inicio(nuevo_dato)
        elif pos >= self.__size:
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
        nodo_actual = self.ubicar(pos)
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
            El nodo que contiene el dato, o None si no se encuentra.
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
            El nodo en la posición especificada, o None si no se encuentra.
        """
        if 0 <= pos < self.__size:
            return np.take(tuple(self.adelante()), pos, mode='clip')
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
            True si la lista se recorre en orden inverso, False en caso contrario.
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


if __name__ == "__main__":
    lista = ListaDE()

    # 1. Prueba: Inicialización y estado vacío
    print("Prueba 1: Inicialización y estado vacío")
    print(f"¿Está vacía? {lista.es_vacia()} (Esperado: True)")
    print(f"Longitud de la lista: {len(lista)} (Esperado: 0)\n")

    # 2. Prueba: Adición de elementos
    print("Prueba 2: Adición de elementos")
    print(f"Adicionando 10: {lista.adicionar(10)} -> {str(lista)} (Esperado: 10)")
    print(f"Adicionando 20: {lista.adicionar(20)} -> {str(lista)} (Esperado: 10 <=> 20)")
    print(f"Adicionando 30: {lista.adicionar(30)} -> {str(lista)} (Esperado: 10 <=> 20 <=> 30)\n")
    
    # 3. Prueba: Insertar al inicio
    print("Prueba 3: Insertar al inicio")
    print(f"Insertando 5 al inicio: {lista.posicionar(5, 0)} -> {str(lista)} (Esperado: 5 <=> 10 <=> 20 <=> 30)\n")
    
    # 4. Prueba: Insertar en medio
    print("Prueba 4: Insertar en medio")
    print(f"Insertando 15 en medio: {lista.posicionar(15, 2)} -> {str(lista)} (Esperado: 5 <=> 10 <=> 15 <=> 20 <=> 30)\n")
    
    # 5. Prueba: Insertar al final
    print("Prueba 5: Insertar al final")
    print(f"Insertando 35 al final: {lista.posicionar(35, 5)} -> {str(lista)} (Esperado: 5 <=> 10 <=> 15 <=> 20 <=> 30 <=> 35)\n")
    
    # 6. Prueba: Búsqueda de elementos
    print("Prueba 6: Búsqueda de elementos")
    print(f"Buscando 15: {lista.encontrar(15).dato} (Esperado: 15)")
    print(f"Ubicando en posición 3: {lista.ubicar(3).dato} (Esperado: 20)")
    print(f"Buscando 100: {lista.encontrar(100)} (Esperado: None)\n")
    
    # 7. Prueba: Eliminación por dato (existe)
    print("Prueba 7: Eliminación por dato (existe)")
    print(f"Eliminando 15: {lista.remover(15, por_pos=False)} -> {str(lista)} (Esperado: 5 <=> 10 <=> 20 <=> 30 <=> 35)\n")
    
    # 8. Prueba: Eliminación por dato (no existe)
    print("Prueba 8: Eliminación por dato (no existe)")
    print(f"Intentando eliminar 100: {lista.remover(100, por_pos=False)} (Esperado: False)\n")
    
    # 9. Prueba: Eliminación por posición
    print("Prueba 9: Eliminación por posición")
    print(f"Eliminando nodo en posición 3: {lista.remover(3, por_pos=True)} -> {str(lista)} (Esperado: 5 <=> 10 <=> 20 <=> 35)\n")
    
    # 10. Prueba: Eliminar el primer nodo
    print("Prueba 10: Eliminar el primer nodo")
    print(f"Eliminando primer nodo: {lista.remover(0, por_pos=True)} -> {str(lista)} (Esperado: 10 <=> 20 <=> 35)\n")
    
    # 11. Prueba: Eliminar el último nodo
    print("Prueba 11: Eliminar el último nodo")
    print(f"Eliminando último nodo: {lista.remover(2, por_pos=True)} -> {str(lista)} (Esperado: 10 <=> 20)\n")
    
    # 12. Prueba: Operaciones con lista de 1 nodo
    print("Prueba 12: Operaciones con lista de 1 nodo")
    print(f"Eliminando único nodo restante: {lista.remover(1, por_pos=True)} -> {str(lista)} (Esperado: 10)")
    print(f"Eliminando último nodo de la lista: {lista.remover(0, por_pos=True)} -> {lista.es_vacia()} (Esperado: True)\n")
    
    # 13. Prueba: Recorridos en modo inverso
    print("Prueba 13: Recorridos en modo inverso")
    lista.adicionar(50)
    lista.adicionar(60)
    lista.adicionar(70)
    lista.inverso = True
    print(f"Recorrido inverso: {[nodo.dato for nodo in lista]} (Esperado: [70, 60, 50])")
    lista.inverso = False
    print(f"Recorrido hacia adelante: {[nodo.dato for nodo in lista]} (Esperado: [50, 60, 70])\n")
    
    # 14. Prueba: Tamaño de la lista en diferentes estados
    print("Prueba 14: Tamaño de la lista en diferentes estados")
    print(f"Tamaño actual: {len(lista)} (Esperado: 3)")
    lista.remover(1, por_pos=True)
    print(f"Tamaño después de la eliminación: {len(lista)} (Esperado: 2)\n")
    
    # 15. Prueba: Agregar y eliminar repetidamente
    print("Prueba 15: Agregar y eliminar repetidamente")
    for i in range(1, 11): 
        lista.adicionar(i)
    print(f"Tamaño después de múltiples adiciones: {len(lista)} (Esperado: 11)")
    for _ in range(5): 
        lista.remover(0, por_pos=True)
    print(f"Tamaño después de múltiples eliminaciones: {len(lista)} (Esperado: 6)\n")
    
    # 16. Prueba: Adiciones y eliminaciones alternas
    print("Prueba 16: Adiciones y eliminaciones alternas")
    lista.adicionar(100)
    print(f"Eliminando 100: {lista.remover(100, por_pos=False)} (Esperado: True)")
    print(f"Eliminando 60: {lista.remover(60, por_pos=False)} (Esperado: True)\n")
    
    print("Todas las pruebas extensivas se completaron.")
