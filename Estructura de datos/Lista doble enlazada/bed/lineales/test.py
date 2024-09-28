import unittest
from lde import Lista_DE

class TestListaDE(unittest.TestCase):
    
    def setUp(self):
        self.lista = Lista_DE()

    def test_lista_vacia(self):
        self.assertTrue(self.lista.es_vacia())
        self.assertEqual(len(self.lista), 0)

    def test_adicionar(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.assertEqual(str(self.lista), "1 <=> 2 <=> 3")
        self.assertEqual(len(self.lista), 3)

    def test_posicionar_inicio(self):
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.lista.posicionar(1, 0)
        self.assertEqual(str(self.lista), "1 <=> 2 <=> 3")

    def test_posicionar_final(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.posicionar(3, 2)
        self.assertEqual(str(self.lista), "1 <=> 2 <=> 3")

    def test_remover_por_posicion(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.lista.remover(1)  # Elimina el nodo en la posición 1 (dato: 2)
        self.assertEqual(str(self.lista), "1 <=> 3")
        self.assertEqual(len(self.lista), 2)

    def test_remover_por_dato(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.lista.remover(2, por_pos=False)  # Elimina el nodo con dato 2
        self.assertEqual(str(self.lista), "1 <=> 3")
        self.assertEqual(len(self.lista), 2)

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
        nodo = self.lista.ubicar(1)  # Ubica el nodo en la posición 1
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.dato, 2)

    def test_adelante(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        datos = [nodo.dato for nodo in self.lista.adelante()]
        self.assertEqual(datos, [1, 2, 3])

    def test_atras(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        datos = [nodo.dato for nodo in self.lista.atras()]
        self.assertEqual(datos, [3, 2, 1])

    def test_inverso(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        self.lista.inverso = True
        datos = [nodo.dato for nodo in self.lista]
        self.assertEqual(datos, [3, 2, 1])

    def test_iterable(self):
        self.lista.adicionar(1)
        self.lista.adicionar(2)
        self.lista.adicionar(3)
        datos = [nodo.dato for nodo in self.lista]
        self.assertEqual(datos, [1, 2, 3])

    def test_adicionar_homogeneidad(self):
        self.lista.adicionar(1)
        with self.assertRaises(ValueError):  
            self.lista.adicionar("XD")

    def test_posicionar_homogeneidad(self):
        self.lista.adicionar(1)
        with self.assertRaises(ValueError): 
            self.lista.posicionar(2.2, 1)


if __name__ == '__main__':
    unittest.main()
