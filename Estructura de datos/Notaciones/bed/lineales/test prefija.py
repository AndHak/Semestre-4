import unittest
from notaciones import Prefija

class TestPrefija(unittest.TestCase):

    def test_infija(self):
        expresion = "3+5*2"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "3 + 5 * 2"
        self.assertEqual(resultado, esperado)

        expresion = "(3+5)*2"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "( 3 + 5 ) * 2"
        self.assertEqual(resultado, esperado)

        expresion = "3+5^2"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "3 + 5 ^ 2"
        self.assertEqual(resultado, esperado)

        expresion = "123456"
        prefija = Prefija(expresion)
        resultado = prefija.infija()
        esperado = "123456"
        self.assertEqual(resultado, esperado)

    def test_prefija(self):
        expresion = "3+5*2"
        prefija = Prefija(expresion)
        resultado = prefija.prefija()  # Cambiado a prefija()
        esperado = "+ 3 * 5 2"
        self.assertEqual(resultado, esperado)

        expresion = "(3+5)*2"
        prefija = Prefija(expresion)
        resultado = prefija.prefija()  # Cambiado a prefija()
        esperado = "* + 3 5 2"
        self.assertEqual(resultado, esperado)

        expresion = "3+5^2"
        prefija = Prefija(expresion)
        resultado = prefija.prefija()  # Cambiado a prefija()
        esperado = "+ 3 ^ 5 2"
        self.assertEqual(resultado, esperado)

    def test_eval_expr_aritm(self):
        expresion = "3+5*2"
        prefija = Prefija(expresion)
        resultado = prefija.eval_expr_aritm()  # Cambiado a eval_expr_aritm()
        esperado = 13.0
        self.assertEqual(resultado, esperado)

        expresion = "(3+5)*2"
        prefija = Prefija(expresion)
        resultado = prefija.eval_expr_aritm()  # Cambiado a eval_expr_aritm()
        esperado = 16.0
        self.assertEqual(resultado, esperado)

        expresion = "3+5^2"
        prefija = Prefija(expresion)
        resultado = prefija.eval_expr_aritm()  # Cambiado a eval_expr_aritm()
        esperado = 28.0
        self.assertEqual(resultado, esperado)

        expresion = "10 + 20 - 30 * 40 / 50"
        prefija = Prefija(expresion)
        resultado = prefija.eval_expr_aritm()  # Cambiado a eval_expr_aritm()
        esperado = 6.0
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
