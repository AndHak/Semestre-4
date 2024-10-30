import unittest
from bed.lineales.pila import Pila
from bed.lineales.cola import Cola

class TestPila(unittest.TestCase):
    
    def setUp(self):
        self.pila = Pila()

    def test_pila_vacia(self):
        print("\nPrueba: Pila vacía")
        resultado_obtenido = self.pila.es_vacia()
        resultado_esperado = True
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = self.pila.cima()
        resultado_esperado = None
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = len(self.pila)
        resultado_esperado = 0
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_apilar(self):
        print("\nPrueba: Apilar elementos")
        self.pila.apilar(1)
        self.pila.apilar(2)
        self.pila.apilar(3)

        resultado_obtenido = self.pila.cima()
        resultado_esperado = 3
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = len(self.pila)
        resultado_esperado = 3
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_desapilar(self):
        print("\nPrueba: Desapilar elementos")
        self.pila.apilar(1)
        self.pila.apilar(2)
        self.pila.apilar(3)

        resultado_obtenido = self.pila.desapilar()
        resultado_esperado = 3
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = len(self.pila)
        resultado_esperado = 2
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_homogeneidad(self):
        print("\nPrueba: Homogeneidad de datos en la pila")
        self.pila.apilar(1)
        resultado_obtenido = self.pila.apilar("XD")
        resultado_esperado = False
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)
        
        resultado_obtenido = len(self.pila)
        resultado_esperado = 1
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_str(self):
        print("\nPrueba: Representación en cadena de la pila")
        self.pila.apilar(1)
        self.pila.apilar(2)
        self.pila.apilar(3)

        resultado_obtenido = str(self.pila)
        resultado_esperado = "===(c)===\n(*[3]*)\n::\n(2)\n::\n(1)"
        print(f"Obtenido: {resultado_obtenido}\nEsperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_intensivo_pila(self):
        print("\nPrueba intensiva: Apilado y desapilado")

        # Probar apilado de múltiples tipos de elementos
        self.pila.apilar(1)
        self.pila.apilar(2)
        self.pila.apilar(3)
        self.pila.apilar(4)
        
        resultado_obtenido = len(self.pila)
        resultado_esperado = 4
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        # Probar homogeneidad en tipos de datos
        resultado_obtenido = self.pila.apilar("XD")
        resultado_esperado = False 
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        # Desapilar elementos uno por uno y verificar
        for i in range(4, 0, -1):
            resultado_obtenido = self.pila.desapilar()
            resultado_esperado = i
            print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
            self.assertEqual(resultado_obtenido, resultado_esperado)

        # Verificar si la pila está vacía después de la operación
        resultado_obtenido = self.pila.es_vacia()
        resultado_esperado = True
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_homogeneidad_pila(self):
        print("\nPrueba: Homogeneidad de tipos en Pila")
        
        # Solo enteros
        self.pila.apilar(1)
        self.pila.apilar(2)

        resultado_obtenido = self.pila.apilar(3.5) 
        resultado_esperado = False 
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = self.pila.apilar("Texto") 
        resultado_esperado = False  
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_pila_varios_tipos(self):
        pila_int = Pila(int)
        pila_str = Pila(str)
        pila_mixta = Pila() # Sin restricción de tipo

        # Prueba con enteros
        pila_int.apilar(10)
        pila_int.apilar(20)
        self.assertEqual(pila_int.desapilar(), 20)
        self.assertEqual(len(pila_int), 1)

        with self.assertRaises(TypeError):  #Prueba de manejo de excepciones
            pila_int.apilar("texto")

        # Prueba con strings
        pila_str.apilar("hola")
        pila_str.apilar("mundo")
        self.assertEqual(pila_str.desapilar(), "mundo")
        self.assertEqual(len(pila_str), 1)

        with self.assertRaises(TypeError):
            pila_str.apilar(123)

        # Prueba con tipos mixtos
        pila_mixta.apilar(10)
        pila_mixta.apilar("hola")
        pila_mixta.apilar(3.14)
        self.assertEqual(pila_mixta.desapilar(), 3.14)
        self.assertEqual(len(pila_mixta), 2)

class TestCola(unittest.TestCase):
    
    def setUp(self):
        self.cola = Cola()

    def test_cola_vacia(self):
        print("\nPrueba: Cola vacía")
        resultado_obtenido = self.cola.es_vacia()
        resultado_esperado = True
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = self.cola.frente()
        resultado_esperado = None
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = len(self.cola)
        resultado_esperado = 0
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_encolar(self):
        print("\nPrueba: Encolar elementos")
        self.cola.encolar(1)
        self.cola.encolar(2)
        self.cola.encolar(3)

        resultado_obtenido = self.cola.frente()
        resultado_esperado = 1
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = len(self.cola)
        resultado_esperado = 3
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_desencolar(self):
        print("\nPrueba: Desencolar elementos")
        self.cola.encolar(1)
        self.cola.encolar(2)
        self.cola.encolar(3)

        resultado_obtenido = self.cola.desencolar()
        resultado_esperado = 1
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = len(self.cola)
        resultado_esperado = 2
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_str(self):
        print("\nPrueba: Representación en cadena de la cola")
        self.cola.encolar(1)
        self.cola.encolar(2)
        self.cola.encolar(3)

        resultado_obtenido = str(self.cola)
        resultado_esperado = "@|<-{1}<-[2]<-[3]"
        print(f"Obtenido: {resultado_obtenido}\nEsperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_intensivo_cola(self):
        print("\nPrueba intensiva: Encolado y desencolado")

        # Probar encolado de múltiples elementos
        for i in range(1, 101): 
            self.cola.encolar(i)
        
        resultado_obtenido = len(self.cola)
        resultado_esperado = 100
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        # Probar homogeneidad en tipos de datos
        resultado_obtenido = self.cola.encolar("XD")
        resultado_esperado = False 
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        # Desencolar elementos y verificar
        for i in range(1, 101):
            resultado_obtenido = self.cola.desencolar()
            resultado_esperado = i
            print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
            self.assertEqual(resultado_obtenido, resultado_esperado)

        # Verificar si la cola está vacía después de la operación
        resultado_obtenido = self.cola.es_vacia()
        resultado_esperado = True
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_homogeneidad_cola(self):
        print("\nPrueba: Homogeneidad de tipos en Cola")
        
        # Solo enteros
        self.cola.encolar(1)
        self.cola.encolar(2)

        resultado_obtenido = self.cola.encolar(3.5)  
        resultado_esperado = False 
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

        resultado_obtenido = self.cola.encolar("Texto") 
        resultado_esperado = False 
        print(f"Obtenido: {resultado_obtenido}, Esperado: {resultado_esperado}")
        self.assertEqual(resultado_obtenido, resultado_esperado)

    def test_cola_varios_tipos(self):
        cola_int = Cola(int)
        cola_str = Cola(str)
        cola_mixta = Cola()

        #Prueba con enteros
        cola_int.encolar(10)
        cola_int.encolar(20)
        self.assertEqual(cola_int.desencolar(), 10)
        self.assertEqual(len(cola_int), 1)

        with self.assertRaises(TypeError):
            cola_int.encolar("texto")

        # Prueba con strings
        cola_str.encolar("hola")
        cola_str.encolar("mundo")
        self.assertEqual(cola_str.desencolar(), "hola")
        self.assertEqual(len(cola_str), 1)

        with self.assertRaises(TypeError):
            cola_str.encolar(123)

        # Prueba con tipos mixtos
        cola_mixta.encolar(10)
        cola_mixta.encolar("hola")
        cola_mixta.encolar(3.14)
        self.assertEqual(cola_mixta.desencolar(), 10)
        self.assertEqual(len(cola_mixta), 2)


if __name__ == '__main__':
    unittest.main()