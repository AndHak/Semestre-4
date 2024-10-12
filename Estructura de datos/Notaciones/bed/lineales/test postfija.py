import unittest
from postfija_sin import Postfija

class TestPostfija(unittest.TestCase):

    def test_infija(self):
        # Prueba 1: Expresión infija simple con números y operadores
        expresion = "3+5*2"
        postfija = Postfija(expresion)
        resultado = postfija.infija()
        esperado = "3 + 5 * 2"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 2: Expresión infija con paréntesis
        expresion = "(3+5)*2"
        postfija = Postfija(expresion)
        resultado = postfija.infija()
        esperado = "( 3 + 5 ) * 2"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 3: Expresión infija con exponentes
        expresion = "3+5^2"
        postfija = Postfija(expresion)
        resultado = postfija.infija()
        esperado = "3 + 5 ^ 2"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 4: Expresión infija solo con números
        expresion = "123456"
        postfija = Postfija(expresion)
        resultado = postfija.infija()
        esperado = "123456"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

    def test_postfija(self):
        # Prueba 1: Expresión infija simple con suma y multiplicación
        expresion = "3+5*2"
        postfija = Postfija(expresion)
        resultado = postfija.postfija()
        esperado = "3 5 2 * +"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 2: Expresión infija con paréntesis
        expresion = "(3+5)*2"
        postfija = Postfija(expresion)
        resultado = postfija.postfija()
        esperado = "3 5 + 2 *"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 3: Expresión infija con exponentes
        expresion = "3+5^2"
        postfija = Postfija(expresion)
        resultado = postfija.postfija()
        esperado = "3 5 2 ^ +"
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

    def test_eval_expr_aritm(self):
        # Prueba 1: Evaluar expresión aritmética simple
        expresion = "3+5*2"
        postfija = Postfija(expresion)
        resultado = postfija.eval_expr_aritm()
        esperado = 13.0
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 2: Evaluar expresión con paréntesis
        expresion = "(3+5)*2"
        postfija = Postfija(expresion)
        resultado = postfija.eval_expr_aritm()
        esperado = 16.0
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 3: Evaluar expresión con exponentes
        expresion = "3+5^2"
        postfija = Postfija(expresion)
        resultado = postfija.eval_expr_aritm()
        esperado = 28.0
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

        # Prueba 4: Evaluar expresión con múltiples operadores
        expresion = "10 + 20 - 30 * 40 / 50"
        postfija = Postfija(expresion)
        resultado = postfija.eval_expr_aritm()
        esperado = 6.0  # Resultado de la expresión
        self.assertEqual(resultado, esperado, f"Error: esperado {esperado}, obtenido {resultado}")

if __name__ == '__main__':
    unittest.main()
