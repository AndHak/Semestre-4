#Integrantes
#Valentina Melo Solarte
#Miguel Angel Narvaez Portilla

if __name__ == "__main__" and __package__ is None:
    from pila import Pila
else:
    from bed.lineales.pila import Pila

class Postfija:
    def __init__(self, expresion_infija: str):
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
            "*": (2, 2), 
            "/": (2, 2), 
            "+": (1, 1), 
            "-": (1, 1), 
            "(": (5, 0)
        }
        resultado = []
        pila_operadores = Pila()
        expresion_lista = self.infija().split(" ")
        for i in range(len(expresion_lista)):
            if expresion_lista[i] == ")":
                desapilado = pila_operadores.desapilar()
                while desapilado != "(":
                    resultado.append(desapilado)
                    desapilado = pila_operadores.desapilar()
            elif expresion_lista[i] in operadores:
                while not pila_operadores.es_vacia() and operadores[expresion_lista[i]][0] <= operadores[pila_operadores.cima()][1]:
                    resultado.append(pila_operadores.desapilar())
                pila_operadores.apilar(expresion_lista[i])
            else:
                resultado.append(expresion_lista[i])
        while not pila_operadores.es_vacia():
            resultado.append(pila_operadores.desapilar())
                    
        return " ".join(resultado)

    def eval_expr_aritm(self):
        expresion = self.postfija().split(" ")
        operadores = ("^", "*", "/", "+", "-")
        pila_operandos = Pila()
        for caracter in expresion:
            if not caracter in operadores:
                pila_operandos.apilar(caracter)
            else:
                if len(pila_operandos) >= 2:
                    operador = "**" if caracter == "^" else caracter
                    operando_2 = pila_operandos.desapilar()
                    operando_1 = pila_operandos.desapilar()
                    resultado = eval(f"{operando_1}{operador}{operando_2}")
                    pila_operandos.apilar(resultado)
                            
        return pila_operandos.desapilar()