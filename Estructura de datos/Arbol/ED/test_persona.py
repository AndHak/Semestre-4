from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.exepciones import HomogeneityError, DuplicatedKeyError
from bed.jerarquicas.recorrido import str_pre_orden, str_in_orden, str_post_orden
from persona import Persona



# Clase adicional para el test
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre}; Precio: {self.precio}"
    
    def __lt__(self, other):
        return self.precio < other.precio
    
    def __eq__(self, other):
        return self.precio == other.precio

def test_varios_arboles():
    # Crear diccionario de árboles
    arboles = {
        "personas": ArbolBinario_Bus(),
        "productos": ArbolBinario_Bus(),
        "mixto": ArbolBinario_Bus()  # Para insertar ambos tipos y probar restricciones de homogeneidad
    }

    # Insertar instancias de Persona en el árbol de personas
    personas = [
        Persona("Maria", 25), Persona("Carlos", 40), Persona("Ana", 10),
        Persona("Pedro", 30), Persona("Juan", 20), Persona("Elena", 60)
    ]
    for persona in personas:
        arboles["personas"].adicionar(persona)

    # Insertar instancias de Producto en el árbol de productos
    productos = [
        Producto("Laptop", 1500), Producto("Teléfono", 800), Producto("Televisor", 600),
        Producto("Teclado", 50), Producto("Monitor", 200), Producto("Mouse", 20)
    ]
    for producto in productos:
        arboles["productos"].adicionar(producto)

    # Insertar ambos tipos en el árbol mixto para probar el manejo de errores de homogeneidad
    try:
        arboles["mixto"].adicionar(personas[0])  # Maria
        arboles["mixto"].adicionar(productos[0])  # Laptop
    except HomogeneityError as e:
        print(f"Error de homogeneidad capturado: {e}")

    # Pruebas sobre los árboles
    for key, arbol in arboles.items():
        print(f"\n--- Árbol de {key} ---")
        print("Recorrido pre-orden:", str_pre_orden(arbol))
        print("Recorrido in-orden:", str_in_orden(arbol))
        print("Recorrido post-orden:", str_post_orden(arbol))

        # Buscar máximos y mínimos
        print("Máximo:", arbol.encontrar_maximo())
        print("Mínimo:", arbol.encontrar_minimo())

        # Otros detalles
        print("Altura del árbol:", arbol.altura())
        print("Cantidad de nodos:", len(arbol))
        print("Hojas del árbol:", arbol.hojas())
        print("Nodos internos:", arbol.internos())

        # Búsqueda de elementos específicos
        if key == "personas":
            print("Buscar a Ana (Edad 10):", arbol.encontrar(Persona("Ana", 10)))
        elif key == "productos":
            print("Buscar Televisor (Precio 600):", arbol.encontrar(Producto("Televisor", 600)))

if __name__ == "__main__":
    test_varios_arboles()
