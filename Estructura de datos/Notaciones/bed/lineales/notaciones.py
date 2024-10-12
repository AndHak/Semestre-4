from pila import Pila
from lse import Lista_SE

class Prefija:
    def __init__(self, expresion_infija: str):
        self.expresion_infija = expresion_infija

    def infija(self) -> str:
        lista = Lista_SE()
        operadores = "+-*/^()"
        numero_actual = ""
        
        for caracter in self.expresion_infija:
            if caracter.isspace():
                continue
            
            if caracter in operadores:
                if numero_actual:
                    lista.adicionar(numero_actual)
                    numero_actual = ""
                lista.adicionar(caracter)
            elif caracter.isdigit():
                numero_actual += caracter
            else:
                if numero_actual:
                    lista.adicionar(numero_actual)
                    numero_actual = ""
                lista.adicionar(caracter)
        
        if numero_actual:
            lista.adicionar(numero_actual)
        
        return " ".join(str(item) for item in lista)


    def prefija(self) -> str:
        pila = Pila()
        salida = Lista_SE()
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
        for token in self.infija().split():
            if token.isdigit() or (token[0] == '-' and len(token) > 1 and token[1:].isdigit()):
                salida.adicionar(token)
            elif token == '(':
                pila.apilar(token)
            elif token == ')':
                while not pila.es_vacia() and pila.cima() != '(':
                    salida.adicionar(pila.desapilar())
                if not pila.es_vacia() and pila.cima() == '(':
                    pila.desapilar()
            else:
                while (not pila.es_vacia() and pila.cima() != '(' and
                       precedencia.get(pila.cima(), 0) >= precedencia.get(token, 0)):
                    salida.adicionar(pila.desapilar())
                pila.apilar(token)
        
        while not pila.es_vacia():
            salida.adicionar(pila.desapilar())
        
        return " ".join(str(item) for item in reversed(list(salida)))

    def eval_expr_aritm(self) -> float:
        pila = Pila()
        
        for token in self.prefija().split():
            if token.isdigit() or (token[0] == '-' and len(token) > 1 and token[1:].isdigit()):
                pila.apilar(float(token))
            else:
                b = pila.desapilar()
                a = pila.desapilar()
                if token == '+':
                    pila.apilar(a + b)
                elif token == '-':
                    pila.apilar(a - b)
                elif token == '*':
                    pila.apilar(a * b)
                elif token == '/':
                    pila.apilar(a / b)
                elif token == '^':
                    pila.apilar(a ** b)
        
        return pila.desapilar()
