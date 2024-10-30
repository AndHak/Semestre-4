
# Prefija
# Clase que implementa la transformación de un expresión matemática Infija a Prefija (notación Polaca)
# y el cálculo de la expresión aritmética Prefija. Los operandos utilizados serán de cualquier cantidad de dígitos.
# Operadores Válidos:       
# + : Suma        
# - : Resta        
# * : Multiplicación       
# / : División        
# ^ : Potenciación        
# ( : Paréntesis Izquierdo        
#  ) : Paréntesis Derecho

#__init__(self, expresión_infija:str)


# infija(self) Método que retorna la expresión Infija original, separando 
# cada operando y cada operador, incluyendo los paréntesis, por un espacio 
# en blanco.      return str


# prefija(self) Método que convierte una expresión Infija a una expresión 
# Prefija, haciendo uso de una Pila. Separar operandos y operadores por un 
# espacio en blanco.      return str


# eval_expr_aritm(self) Evaluación de la expresión aritmética en notación 
# Prefija, utilizando una Pila, calculando el resultado final de la expresión.
#       return float

from pila import Pila
from lse import Lista_SE


class Prefija:
    def __init__(self, expresion_infija: str):
        self.expresion_infija = expresion_infija

    def infija(self) -> str:
        resultado = []
        operadores = ('+', '-', '*', '/', '^', '(', ')')
        i = 0
        while i < len(self.expresion_infija):
            if self.expresion_infija[i] in operadores:
                resultado.append(self.expresion_infija[i])
            elif self.expresion_infija[i].isdigit():
                numeros = []
                while i < len(self.expresion_infija) and self.expresion_infija[i].isdigit():
                    numeros.append(self.expresion_infija[i])
                    i += 1
                resultado.append("".join(numeros))
                continue
            i += 1
        return " ".join(resultado)

    def prefija(self) -> str:
        operadores = {
            "^": (4, 3),
            "*": (2, 2),
            "/": (2, 2),
            "+": (1, 1),
            "-": (1, 1),
            "(": (5, 0)
        }
        resultado = []
        pila_operadores = Pila()
        expresion_lista = self.infija().split(" ")
        
        for i in reversed(range(len(expresion_lista))-1,-1):
            expresion_lista[i]
            if expresion_lista[i] == "(":
                desapilado = pila_operadores.desapilar()
                while desapilado != ")":
                    resultado.append(desapilado)
                    desapilado = pila_operadores.desapilar()
            elif expresion_lista[i] in operadores:
                while not pila_operadores.es_vacia() and operadores[expresion_lista[i]][0] < operadores[pila_operadores.cima()][1]:
                    resultado.append(pila_operadores.desapilar())
                pila_operadores.apilar(expresion_lista[i])
            else:
                resultado.append(expresion_lista[i])

        while not pila_operadores.es_vacia():
            resultado.append(pila_operadores.desapilar())
        return " ".join(reversed(resultado))



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

