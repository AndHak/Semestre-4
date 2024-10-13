
from pila import Pila

class Postfija:
    def __init__(self, expresion_infija=str):
        self.expresion_infija = expresion_infija
    
    def infija(self):
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
          
    def postfija(self):
        operadores = {  
            "^": (4, 3),  
            "*": (3, 2),  
            "/": (3, 2),  
            "+": (2, 1),  
            "-": (2, 1),  
            "(": (1, 0)  
        }  
        resultado = []  
        pila_operadores = Pila()  
        expresion_lista = self.infija().split(" ")[::-1]  # Reversar la expresión infija  

        for token in expresion_lista:  
            if token == ")":  
                pila_operadores.apilar(token)  
            elif token == "(":  
                while not pila_operadores.es_vacia() and pila_operadores.cima() != ")":  
                    resultado.append(pila_operadores.desapilar())  
                pila_operadores.desapilar()  # Desapilar ")"  
            elif token in operadores:  
                while (not pila_operadores.es_vacia() and  
                       operadores[token][0] < operadores[pila_operadores.cima()][1]):  
                    resultado.append(pila_operadores.desapilar())  
                pila_operadores.apilar(token)  
            else:  
                resultado.append(token)  

        while not pila_operadores.es_vacia():  
            resultado.append(pila_operadores.desapilar())  
            
        return " ".join(reversed(resultado)) 

    def eval_expr_aritm(self):
        expresion = self.postfija().split(" ")
        operadores = ("^", "*", "/", "+", "-")
        pila_operandos = Pila()
        
        for caracter in expresion:
            if caracter not in operadores:
                pila_operandos.apilar(float(caracter)) 
            else:
                operando_2 = pila_operandos.desapilar() 
                operando_1 = pila_operandos.desapilar()  
                
                if caracter == "+":
                    resultado = operando_1 + operando_2
                elif caracter == "-":
                    resultado = operando_1 - operando_2
                elif caracter == "*":
                    resultado = operando_1 * operando_2
                elif caracter == "/":
                    resultado = operando_1 / operando_2
                elif caracter == "^":
                    resultado = operando_1 ** operando_2
                
               
                pila_operandos.apilar(resultado)  
        
        return pila_operandos.desapilar()  