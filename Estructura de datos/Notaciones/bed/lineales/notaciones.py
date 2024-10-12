from pila import Pila
from lse import Lista_SE

class Prefija:
    def __init__(self, expresion_infija: str):
        self.expresion_infija = expresion_infija

    def infija(self) -> str:
        resultado = Lista_SE()
        operadores = ('+', '-', '*', '/', '^', '(', ')')
        i = 0
        while i < len(self.expresion_infija):
            if self.expresion_infija[i] in operadores:
                resultado.adicionar(self.expresion_infija[i]) 
            elif self.expresion_infija[i].isdigit():
                numeros = Lista_SE()
                while i < len(self.expresion_infija) and self.expresion_infija[i].isdigit():
                    numeros.adicionar(self.expresion_infija[i])  
                    i += 1
                resultado.adicionar("".join(numeros))
                continue
            i += 1
        return " ".join(resultado) 

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
        expresion = self.prefija().split()  
        operadores = {"^", "*", "/", "+", "-"}
        pila_operandos = Pila()

        for token in reversed(expresion):
            if token not in operadores:
                pila_operandos.apilar(float(token))
            else:
                operando_1 = pila_operandos.desapilar()
                operando_2 = pila_operandos.desapilar()

                if token == "+":
                    resultado = operando_1 + operando_2
                elif token == "-":
                    resultado = operando_1 - operando_2
                elif token == "*":
                    resultado = operando_1 * operando_2
                elif token == "/":
                    resultado = operando_1 / operando_2
                elif token == "^":
                    resultado = operando_1 ** operando_2

                pila_operandos.apilar(resultado)

        return pila_operandos.desapilar()
