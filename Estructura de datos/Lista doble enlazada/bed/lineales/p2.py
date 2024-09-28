
from nodos import NodoListaDE

class ListaDE:
    """Lista doblemente enlazada."""

    def __init__(self):
        self.__head = self.__tail = None
        self.__size = 0
        self.__inverso = False

    def es_vacia(self) -> bool:
        return self.__head is None

    def adicionar(self, nuevo_dato) -> bool:
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
        if pos <= 0:
            return self.__insertar_inicio(nuevo_dato)
        elif pos >= self.__size:
            return self.adicionar(nuevo_dato)
        else:
            nodo_actual = self.ubicar(pos)
            nuevo_nodo = NodoListaDE(nuevo_dato, siguiente=nodo_actual, anterior=nodo_actual.anterior)
            if nodo_actual.anterior:
                nodo_actual.anterior.siguiente = nuevo_nodo
            nodo_actual.anterior = nuevo_nodo
            if nodo_actual == self.__head:  # Si se inserta al principio
                self.__head = nuevo_nodo
            self.__size += 1
            return True

    def __insertar_inicio(self, nuevo_dato):
        nuevo_nodo = NodoListaDE(nuevo_dato, siguiente=self.__head)
        if self.__head:
            self.__head.anterior = nuevo_nodo
        self.__head = nuevo_nodo
        if self.es_vacia():  # Si estaba vacía, también es la cola
            self.__tail = nuevo_nodo
        self.__size += 1
        return True

    def remover(self, item, por_pos=True) -> bool:
        nodo_actual = self.ubicar(item) if por_pos else self.encontrar(item)
        if nodo_actual: 
            self.__remove_node(nodo_actual)
            return True
        return False

    def __remove_node(self, nodo):
        if nodo.anterior: 
            nodo.anterior.siguiente = nodo.siguiente
        if nodo.siguiente: 
            nodo.siguiente.anterior = nodo.anterior
        self.__head = self.__head.siguiente if nodo == self.__head else self.__head
        self.__tail = self.__tail.anterior if nodo == self.__tail else self.__tail
        self.__size -= 1

    def encontrar(self, dato_buscar) -> object:
        return next((n for n in self.adelante() if n.dato == dato_buscar), None)

    def ubicar(self, pos) -> object:
        nodo_actual = self.__head
        for _ in range(pos): 
            nodo_actual = nodo_actual.siguiente
        return nodo_actual if 0 <= pos < self.__size else None

    def adelante(self):
        nodo_actual = self.__head
        while nodo_actual: 
            yield nodo_actual
            nodo_actual = nodo_actual.siguiente

    def atras(self):
        nodo_actual = self.__tail
        while nodo_actual: 
            yield nodo_actual
            nodo_actual = nodo_actual.anterior

    def __str__(self) -> str:
        return " <=> ".join(str(nodo.dato) for nodo in self.adelante())

    @property
    def inverso(self) -> bool:
        return self.__inverso

    @inverso.setter
    def inverso(self, valor: bool):
        self.__inverso = valor

    def __len__(self) -> int:
        return self.__size

    def __iter__(self):
        return self.atras() if self.__inverso else self.adelante()

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
