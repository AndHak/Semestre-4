import unittest
from bed.jerarquicas.abin_bus import ArbolBinario_Bus
from bed.jerarquicas.exepciones import HomogeneityError, DuplicatedKeyError
from bed.jerarquicas.recorrido import str_pre_orden, str_in_orden, str_post_orden

class TestArbolBinarioBus(unittest.TestCase):

    def setUp(self):
        """Configuración inicial: se crea un árbol binario de búsqueda vacío."""
        self.arbol = ArbolBinario_Bus()

    def test_adicionar_y_encontrar(self):
        """Prueba la adición y búsqueda de claves en el árbol binario de búsqueda."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)

        # Verificación de claves
        print("Esperado: 50, Obtenido:", self.arbol.encontrar(50))
        self.assertEqual(self.arbol.encontrar(50), 50)

        print("Esperado: 30, Obtenido:", self.arbol.encontrar(30))
        self.assertEqual(self.arbol.encontrar(30), 30)

        print("Esperado: 70, Obtenido:", self.arbol.encontrar(70))
        self.assertEqual(self.arbol.encontrar(70), 70)

        print("Esperado: None, Obtenido:", self.arbol.encontrar(40))
        self.assertIsNone(self.arbol.encontrar(40))

    def test_adicionar_duplicado(self):
        """Prueba que se levante la excepción DuplicatedKeyError al agregar un valor duplicado."""
        self.arbol.adicionar(50)
        print("Esperado: DuplicatedKeyError")
        with self.assertRaises(DuplicatedKeyError):
            self.arbol.adicionar(50)

    def test_tipo_incorrecto(self):
        """Prueba que se levante la excepción HomogeneityError al agregar un tipo de dato distinto."""
        self.arbol.adicionar(50)
        print("Esperado: HomogeneityError al añadir un tipo distinto (string)")
        with self.assertRaises(HomogeneityError):
            self.arbol.adicionar("string")

    def test_encontrar_minimo_y_maximo(self):
        """Prueba la búsqueda de la clave mínima y máxima en el árbol."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)
        self.arbol.adicionar(10)
        self.arbol.adicionar(90)

        print("Esperado mínimo: 10, Obtenido:", self.arbol.encontrar_minimo())
        self.assertEqual(self.arbol.encontrar_minimo(), 10)

        print("Esperado máximo: 90, Obtenido:", self.arbol.encontrar_maximo())
        self.assertEqual(self.arbol.encontrar_maximo(), 90)

    def test_remover_nodo_sin_hijos(self):
        """Prueba la eliminación de un nodo sin hijos."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)
        self.arbol.remover(30)

        print("Esperado: None, Obtenido:", self.arbol.encontrar(30))
        self.assertIsNone(self.arbol.encontrar(30))

    def test_remover_nodo_con_un_hijo(self):
        """Prueba la eliminación de un nodo con un hijo."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(40)  # Nodo 30 tiene un solo hijo, 40
        self.arbol.remover(30)

        print("Esperado encontrar None en nodo eliminado: Obtenido:", self.arbol.encontrar(30))
        self.assertIsNone(self.arbol.encontrar(30))

        print("Esperado encontrar 40 en árbol: Obtenido:", self.arbol.encontrar(40))
        self.assertEqual(self.arbol.encontrar(40), 40)

    def test_remover_nodo_con_dos_hijos(self):
        """Prueba la eliminación de un nodo con dos hijos."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)
        self.arbol.adicionar(60)
        self.arbol.adicionar(80)

        self.arbol.remover(70)

        print("Esperado: None, Obtenido:", self.arbol.encontrar(70))
        self.assertIsNone(self.arbol.encontrar(70))

    def test_str_pre_orden(self):
        """Prueba de representación en pre-orden con emojis."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)
        self.arbol.adicionar(10)

        esperado = '[🌲]50|(🌿)30|(🍂)10|(🍂)70'
        obtenido = str_pre_orden(self.arbol)
        print(f"Esperado: {esperado}, Obtenido: {obtenido}")
        self.assertEqual(obtenido, esperado)

    def test_str_in_orden(self):
        """Prueba de representación en in-orden con emojis."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)
        self.arbol.adicionar(10)

        esperado = '(🍂)10:(🌿)30:[🌲]50:(🍂)70'
        obtenido = str_in_orden(self.arbol)
        print(f"Esperado: {esperado}, Obtenido: {obtenido}")
        self.assertEqual(obtenido, esperado)

    def test_str_post_orden(self):
        """Prueba de representación en post-orden con emojis."""
        self.arbol.adicionar(50)
        self.arbol.adicionar(30)
        self.arbol.adicionar(70)
        self.arbol.adicionar(10)

        esperado = '(🍂)10^(🌿)30^(🍂)70^[🌲]50'
        obtenido = str_post_orden(self.arbol)
        print(f"Esperado: {esperado}, Obtenido: {obtenido}")
        self.assertEqual(obtenido, esperado)

if __name__ == '__main__':
    unittest.main()
