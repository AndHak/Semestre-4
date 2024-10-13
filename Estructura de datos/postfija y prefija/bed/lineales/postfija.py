
from pila import Pila

class Postfija:
    def __init__(self, expresion_infija=str):
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