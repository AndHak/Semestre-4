from pila import Pila
from lse import Lista_SE

class Prefija:
    def __init__(self, expresion_infija: str):
        self.expresion_infija = expresion_infija

    def infija(self) -> str:
        def recursion(i=0):
            if i == len(self.expresion_infija):
                return ""
            if self.expresion_infija[i].isdigit():
                num = self.expresion_infija[i]
                return num + recursion(i + 1) if i + 1 < len(self.expresion_infija) and self.expresion_infija[i + 1].isdigit() else num + " " + recursion(i + 1)
            return self.expresion_infija[i] + " " + recursion(i + 1)

        return recursion().strip()

    def prefija(self) -> str:
        pila = Pila()
        salida = Lista_SE()
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

        # Recorremos la expresión infija de derecha a izquierda
        for i in reversed(self.infija().split()):
            if i.isdigit() or (i[0] == '-' and len(i) > 1 and i[1:].isdigit()) or '.' in i:
                salida.adicionar(i)  
            elif i == ')':
                pila.apilar(i)
            elif i == '(':
                while not pila.es_vacia() and pila.cima() != ')':
                    salida.adicionar(pila.desapilar())  
                if not pila.es_vacia():  
                    pila.desapilar()
            else: 
                while (not pila.es_vacia() and pila.cima() != ')' and
                       precedencia.get(i, 0) < precedencia.get(pila.cima(), 0)):
                    salida.adicionar(pila.desapilar()) 
                pila.apilar(i)

        while not pila.es_vacia():
            salida.adicionar(pila.desapilar()) 

        salida_lista = []
        for item in salida:
            salida_lista.append(str(item))

        return " ".join(reversed(salida_lista)) 

    def eval_expr_aritm(self) -> float:
        operadores = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y, '/': lambda x, y: x / y, 
                      '^': lambda x, y: x ** y}
        pila = Pila()

        for i in reversed(self.prefija().split()):
            if i.isdigit():
                pila.apilar(float(i))
            else:
                operando_1, operando_2 = pila.desapilar(), pila.desapilar()
                pila.apilar(operadores[i](operando_1, operando_2))

        return pila.desapilar()