import unittest
from cp import ColaPrioridad

class TestColaPrioridadIntensivo(unittest.TestCase):

    def setUp(self):
        """Crea una nueva ColaPrioridad para cada prueba."""
        self.cola_prioridad = ColaPrioridad(5)  # Cola con 5 niveles de prioridad

    def test_encolar_desencolar_grandes_volumenes(self):
        """Prueba con un gran número de elementos."""
        for i in range(1000):
            self.assertTrue(self.cola_prioridad.encolar(i, i % 5))
        self.assertEqual(len(self.cola_prioridad), 1000)
        
        # Desencolamos los elementos y verificamos el orden por prioridad
        elementos = []
        for _ in range(1000):
            elementos.append(self.cola_prioridad.desencolar())
        
        # Verifica que los elementos estén desencolados en el orden correcto por prioridad
        self.assertEqual(elementos[:200], list(range(0, 1000, 5)))  # Prioridad 0
        self.assertEqual(elementos[200:400], list(range(1, 1000, 5)))  # Prioridad 1
        self.assertEqual(elementos[400:600], list(range(2, 1000, 5)))  # Prioridad 2
        self.assertEqual(elementos[600:800], list(range(3, 1000, 5)))  # Prioridad 3
        self.assertEqual(elementos[800:], list(range(4, 1000, 5)))  # Prioridad 4

    def test_mezcla_varias_operaciones(self):
        """Mezcla intensiva de operaciones de encolar, desencolar y frente."""
        self.cola_prioridad.encolar(100, 1)
        self.cola_prioridad.encolar(200, 2)
        self.cola_prioridad.encolar(300, 0)
        self.assertEqual(self.cola_prioridad.frente(), 300)  # Prioridad 0
        self.assertEqual(self.cola_prioridad.desencolar(), 300)  # Desencola prioridad 0
        
        # Mezcla de encolado y desencolado
        self.cola_prioridad.encolar(400, 1)
        self.assertEqual(self.cola_prioridad.frente(), 100)  # Prioridad 1
        self.assertEqual(self.cola_prioridad.desencolar(), 100)  # Prioridad 1
        self.assertEqual(self.cola_prioridad.desencolar(), 400)  # Prioridad 1

        self.cola_prioridad.encolar(500, 3)
        self.assertEqual(self.cola_prioridad.frente(), 200)  # Prioridad 2
        self.assertEqual(self.cola_prioridad.desencolar(), 200)  # Prioridad 2
        self.assertEqual(self.cola_prioridad.desencolar(), 500)  # Prioridad 3

    def test_encolar_prioridad_maxima_minima(self):
        """Prueba encolar en los niveles de prioridad máxima y mínima."""
        self.assertTrue(self.cola_prioridad.encolar(999, 4))  # Prioridad máxima
        self.assertTrue(self.cola_prioridad.encolar(1, 0))  # Prioridad mínima

        self.assertEqual(self.cola_prioridad.desencolar(), 1)  # Prioridad 0 primero
        self.assertEqual(self.cola_prioridad.desencolar(), 999)  # Prioridad 4 después

    def test_desencolar_varios_vacios(self):
        """Prueba desencolar repetidamente cuando está vacía."""
        for _ in range(5):
            self.assertIsNone(self.cola_prioridad.desencolar())

    def test_frente_cuando_vacia(self):
        """Prueba el método frente cuando la cola está vacía."""
        self.assertIsNone(self.cola_prioridad.frente())
        self.cola_prioridad.encolar(50, 3)
        self.assertEqual(self.cola_prioridad.frente(), 50)
        self.cola_prioridad.desencolar()
        self.assertIsNone(self.cola_prioridad.frente())

    def test_str_intensivo(self):
        """Prueba intensiva del método __str__ con varias prioridades."""
        self.cola_prioridad.encolar(1, 0)
        self.cola_prioridad.encolar(2, 1)
        self.cola_prioridad.encolar(3, 2)
        self.cola_prioridad.encolar(4, 3)
        self.cola_prioridad.encolar(5, 4)
        self.assertIn("Prioridad 0: [1]", str(self.cola_prioridad))
        self.assertIn("Prioridad 1: [2]", str(self.cola_prioridad))
        self.assertIn("Prioridad 2: [3]", str(self.cola_prioridad))
        self.assertIn("Prioridad 3: [4]", str(self.cola_prioridad))
        self.assertIn("Prioridad 4: [5]", str(self.cola_prioridad))

    def test_operaciones_complejas(self):
        """Prueba con una combinación compleja de operaciones."""
        for i in range(50):
            self.cola_prioridad.encolar(i, i % 5)
        
        self.assertEqual(self.cola_prioridad.desencolar(), 0)  # Prioridad 0
        self.assertEqual(self.cola_prioridad.desencolar(), 5)  # Prioridad 0

        self.cola_prioridad.encolar(100, 2)
        self.assertEqual(self.cola_prioridad.frente(), 10)  # Prioridad 0, no 1
        self.assertEqual(len(self.cola_prioridad), 49)


if __name__ == '__main__':
    unittest.main()
