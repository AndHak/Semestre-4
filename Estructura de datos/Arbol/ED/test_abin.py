from bed.jerarquicas.abin import arbolBin

def test_arbol_binario():
    # Crear un árbol binario
    arbol = arbolBin()

    # Añadir algunos elementos al árbol
    arbol.adicionar(10)
    arbol.adicionar(5)
    arbol.adicionar(15)
    arbol.adicionar(3)
    arbol.adicionar(7)

    # Comprobar si la raíz tiene hijos
    assert arbol.raiz is not None, "El árbol debería tener una raíz."
    assert arbol.raiz.tiene_hijos(), "La raíz debería tener al menos un hijo."

    # Verificar que los nodos se han añadido
    print("Raíz del árbol:", arbol.raiz)
    if arbol.raiz.izq:
        print("Hijo izquierdo de la raíz:", arbol.raiz.izq)
    if arbol.raiz.der:
        print("Hijo derecho de la raíz:", arbol.raiz.der)

    # Comprobar que algunos hijos también tienen hijos
    if arbol.raiz.izq:
        print("Hijo izquierdo tiene hijos:", arbol.raiz.izq.tiene_hijos())
    if arbol.raiz.der:
        print("Hijo derecho tiene hijos:", arbol.raiz.der.tiene_hijos())

    # Mostrar si se han añadido los nodos de manera aleatoria
    print("Árbol añadido con nodos al azar.")

# Ejecutar el test
# test_arbol_binario()

def test_encontrar_elemento():
    # Crear un árbol binario
    arbol = arbolBin()

    # Añadir algunos elementos al árbol
    arbol.adicionar(10)
    arbol.adicionar(5)
    arbol.adicionar(15)
    arbol.adicionar(3)
    arbol.adicionar(7)

    # Probar si los elementos añadidos están presentes en el árbol
    assert arbol.encontrar(10) == 10, "El elemento 10 debería estar en el árbol."
    print("---------------------------")
    assert arbol.encontrar(5) == 5, "El elemento 5 debería estar en el árbol."
    print("---------------------------")
    
    assert arbol.encontrar(15) == 15, "El elemento 15 debería estar en el árbol."
    print("---------------------------")
    assert arbol.encontrar(3) == 3, "El elemento 3 debería estar en el árbol."
    print("---------------------------")
    assert arbol.encontrar(7) == 7, "El elemento 7 debería estar en el árbol."
    print("---------------------------")
    # Probar valores inexistentes (como el 0 o cualquier otro valor que no se haya añadido)
    
    assert arbol.encontrar(0) is None, "El elemento 0 no debería estar en el árbol."
    print("---------------------------")
    assert arbol.encontrar(20) is None, "El elemento 20 no debería estar en el árbol."
    print("---------------------------")
    assert arbol.encontrar(100) is None, "El elemento 100 no debería estar en el árbol."
    print("---------------------------")
    print("Todos los tests de 'encontrar' pasaron exitosamente.")

    assert len(arbol) == 5, "la cantidad de nodos debio ser 4"

# Ejecutar el test
test_encontrar_elemento()

