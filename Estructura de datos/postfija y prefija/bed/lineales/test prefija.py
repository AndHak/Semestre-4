from notaciones import Prefija
import unittest

class TestPrefija(unittest.TestCase):
    
    def test_infija(self):
        expresion = Prefija("(3+5)*2")
        resultado = expresion.infija()
        self.assertEqual(resultado, "( 3 + 5 ) * 2")

    def test_infija_complex(self):
        expresion = Prefija("3+(4*5)-2")
        resultado = expresion.infija()
        self.assertEqual(resultado, "3 + ( 4 * 5 ) - 2")

    def test_prefija(self):
        expresion = Prefija("(3+5)*2")
        resultado = expresion.prefija()
        self.assertEqual(resultado, "* + 3 5 2")

    def test_prefija_complex(self):
        expresion = Prefija("3+(4*5)-2")
        resultado = expresion.prefija()
        self.assertEqual(resultado, "- + 3 * 4 5 2")

    def test_eval_expr_aritm(self):
        expresion = Prefija("(3+5)*2")
        resultado = expresion.eval_expr_aritm()
        self.assertEqual(resultado, 16)

    def test_eval_expr_aritm_complex(self):
        expresion = Prefija("3+(4*5)-2")
        resultado = expresion.eval_expr_aritm()
        self.assertEqual(resultado, 21)

    def test_eval_expr_with_exponent(self):
        expresion = Prefija("(2^3)+(4*5)-3")
        resultado = expresion.eval_expr_aritm()
        self.assertEqual(resultado, 25)

    def test_eval_expr_with_division(self):
        expresion = Prefija("(10/2)+3")
        resultado = expresion.eval_expr_aritm()
        self.assertEqual(resultado, 8)

if __name__ == '__main__':
    unittest.main()
