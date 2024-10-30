import unittest
from lde import Lista_DE

class TestListaDE(unittest.TestCase):

    def setUp(self):
        self.lista = Lista_DE()

    def test_adicionar(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.assertEqual(str(self.lista), "1 <=> 2 <=> 3")
        self.assertEqual(len(self.lista), 3)

    def test_es_vacia(self):
        self.assertTrue(self.lista.es_vacia())
        self.lista.adicionar(1)
        self.assertFalse(self.lista.es_vacia())

    def test_posicionar(self):
        self.lista.posicionar(1)
        self.lista.posicionar(2)
        self.lista.posicionar(3, 1)
        self.assertEqual(str(self.lista), "1 <=> 3 <=> 2")

    def test_remover(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.lista.remover(1, por_pos=True)
        self.assertEqual(str(self.lista), "1 <=> 3")
        self.lista.remover(1, por_pos=False)
        self.assertEqual(str(self.lista), "3")

    def test_encontrar(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        nodo = self.lista.encontrar(2)
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.dato, 2)

    def test_ubicar(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        nodo = self.lista.ubicar(1)
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.dato, 2)

    def test_inverso(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.lista.inverso = True
        self.assertEqual(" <=> ".join(map(str, (nodo.dato for nodo in self.lista))), "3 <=> 2 <=> 1")

    def test_iter(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.assertEqual([nodo.dato for nodo in self.lista], [1, 2, 3])
        self.lista.inverso = True
        self.assertEqual([nodo.dato for nodo in self.lista], [3, 2, 1])

    # def test_homogeneidad(self):
    #     # Prueba que todos los elementos deben ser del mismo tipo
    #     self.lista.adicionar(1)
    #     self.lista.adicionar(2)
    #     with self.assertRaises(TypeError):
    #         self.lista.adicionar("texto")  # Intentar añadir un string cuando ya hay enteros


if __name__ == '__main__':
    unittest.main()