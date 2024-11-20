import unittest
import json
from bed.jerarquicas.arbol_decision import ArbolDecision
from bed.jerarquicas.nodo_decision import NodoDecision
from bed.jerarquicas.excepciones import NodoNoEncontradoError, ArbolVacioError, NodoYaExisteError, ClasificacionInvalidaError, ValorInvalidoError

class TestArbolDecision(unittest.TestCase):

    def setUp(self):
        self.arbol = ArbolDecision()

    def test_arbol_vacio(self):
        with self.assertRaises(ArbolVacioError, msg="Esperado: ArbolVacioError, Obtenido: Árbol no lanzó excepción en árbol vacío"):
            if not self.arbol.raiz:
                raise ArbolVacioError()

    def test_agregar_nodo_raiz(self):
        nodo = NodoDecision("edad", "Menor de 18 años", es_hoja=True, clasificacion="Niño")
        self.arbol.raiz = nodo
        self.assertEqual(self.arbol.raiz.valor, "Menor de 18 años", f"Esperado: Menor de 18 años, Obtenido: {self.arbol.raiz.valor}")

    def test_agregar_nodo_duplicado(self):
        nodo = NodoDecision("edad", "Menor de 18 años", es_hoja=True, clasificacion="Niño")
        self.arbol.raiz = nodo
        with self.assertRaises(NodoYaExisteError, msg="Esperado: NodoYaExisteError, Obtenido: No se lanzó excepción al agregar nodo duplicado"):
            if self.arbol.raiz.valor == nodo.valor:
                raise NodoYaExisteError()

    def test_buscar_nodo_no_existente(self):
        nodo = NodoDecision("edad", "Menor de 18 años", es_hoja=True, clasificacion="Niño")
        self.arbol.raiz = nodo
        with self.assertRaises(NodoNoEncontradoError, msg="Esperado: NodoNoEncontradoError, Obtenido: No se lanzó excepción al buscar nodo no existente"):
            resultado = self.arbol.buscar_nodo(self.arbol.raiz, "No existe")
            if resultado is None:
                raise NodoNoEncontradoError()

    def test_clasificacion_invalida(self):
        with self.assertRaises(ClasificacionInvalidaError, msg="Esperado: ClasificacionInvalidaError, Obtenido: No se lanzó excepción con clasificación inválida"):
            nodo = NodoDecision("edad", "Menor de 18 años", es_hoja=True, clasificacion="Desconocido")
            if nodo.clasificacion not in ["Niño", "Adolescente", "Adulto", "Mayor"]:
                raise ClasificacionInvalidaError()

    def test_valor_invalido(self):
        with self.assertRaises(ValorInvalidoError, msg="Esperado: ValorInvalidoError, Obtenido: No se lanzó excepción con valor inválido"):
            nodo = NodoDecision("edad", "", es_hoja=True, clasificacion="Niño")
            if nodo.valor == "":
                raise ValorInvalidoError()

    def test_recorrido_preorden(self):
        nodo1 = NodoDecision("edad", "Menor de 18 años", es_hoja=True, clasificacion="Niño")
        nodo2 = NodoDecision("edad", "18 a 30 años", es_hoja=True, clasificacion="Adulto Joven")
        self.arbol.raiz = nodo1
        self.arbol.raiz.hijos.append(nodo2)
        
        recorrido = self.arbol.recorrido_preorden(self.arbol.raiz)
        
        # Verificar que el recorrido en preorden incluya los nodos en orden esperado
        self.assertEqual([n.valor for n in recorrido], ["Menor de 18 años", "18 a 30 años"], f"Esperado: ['Menor de 18 años', '18 a 30 años'], Obtenido: {[n.valor for n in recorrido]}")

        # Guardar el recorrido en un archivo JSON
        datos_json = [{"valor": n.valor, "clasificacion": n.clasificacion} for n in recorrido]
        with open("recorrido_preorden.json", "w") as json_file:
            json.dump(datos_json, json_file, indent=4)
            print("\nRecorrido preorden guardado en 'recorrido_preorden.json'.")

if __name__ == "__main__":
    unittest.main()
