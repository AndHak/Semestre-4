import unittest
from notaciones import Prefija

class TestNotaciones(unittest.TestCase):

    def test_infija(self):
        # Prueba 1: Expresión infija simple con números y operadores
        expresion = "3+5*2"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "(3) :>: (+) :>: (5) :>: (*) :>: (2)"
        self.assertEqual(str(resultado), esperado, f"Error: esperado {esperado}, obtenido {str(resultado)}")

        # Prueba 2: Expresión infija con paréntesis
        expresion = "(3+5)*2"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "(() :>: (3) :>: (+) :>: (5) :>: ()) :>: (*) :>: (2)"
        self.assertEqual(str(resultado), esperado, f"Error: esperado {esperado}, obtenido {str(resultado)}")

        # Prueba 3: Expresión infija con exponentes
        expresion = "3+5^2"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "(3) :>: (+) :>: (5) :>: (^) :>: (2)"
        self.assertEqual(str(resultado), esperado, f"Error: esperado {esperado}, obtenido {str(resultado)}")

        # Prueba 4: Expresión infija solo con números
        expresion = "123456"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "(123456)"
        self.assertEqual(str(resultado), esperado, f"Error: esperado {esperado}, obtenido {str(resultado)}")

        # Prueba 5: Expresión infija con operadores múltiples
        expresion = "10+20-30*40/50"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "(10) :>: (+) :>: (20) :>: (-) :>: (30) :>: (*) :>: (40) :>: (/) :>: (50)"
        self.assertEqual(str(resultado), esperado, f"Error: esperado {esperado}, obtenido {str(resultado)}")

if __name__ == '__main__':
    unittest.main()
