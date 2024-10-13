# ANDRES FELIPE MARTINEZ GUERRA
# SEBASTIAN DAVID ORDOÑEZ BOLAÑOS 
from pila import Pila
from lse import Lista_SE

class Prefija:
    """Clase para manejar expresiones aritméticas en notación infija y convertirlas a notación prefija.

    Parameters
    ----------
    expresion_infija : str
        La expresión aritmética en notación infija (por ejemplo, "(3+5)*2").
    """

    def __init__(self, expresion_infija: str):
        """Inicializa la clase con la expresión infija.

        Parameters
        ----------
        expresion_infija : str
            La expresión en notación infija que se va a procesar.
        """
        self.expresion_infija = expresion_infija

    def infija(self) -> str:
        """Convierte la expresión infija a un formato con espacios entre números y operadores.

        Returns
        -------
        str
            La expresión infija con espacios entre sus componentes.
        """

        def recursion(i=0):
            """Función recursiva para agregar espacios entre números y operadores.

            Parameters
            ----------
            i : int, optional
                Índice actual de la expresión que se está procesando (default is 0).

            Returns
            -------
            str
                La parte procesada de la expresión.
            """
            if i == len(self.expresion_infija):
                return ""
            if self.expresion_infija[i].isdigit():
                num = self.expresion_infija[i]
                return (num + recursion(i + 1) 
                        if i + 1 < len(self.expresion_infija) and self.expresion_infija[i + 1].isdigit() 
                        else num + " " + recursion(i + 1))
            return self.expresion_infija[i] + " " + recursion(i + 1)

        return recursion().strip()

    def prefija(self) -> str:
        """Convierte la expresión infija almacenada en la instancia a notación prefija.

        Returns
        -------
        str
            La expresión en notación prefija.
        """
        pila = Pila()
        salida = Lista_SE()
        precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

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
                while (not pila.es_vacia() and pila.cima() != ')'):
                    precedencia_actual = precedencia[i] if i in precedencia else 0
                    precedencia_cima = precedencia[pila.cima()] if pila.cima() in precedencia else 0

                    if precedencia_actual >= precedencia_cima:
                        break
                    salida.adicionar(pila.desapilar())
                pila.apilar(i)

        while not pila.es_vacia():
            salida.adicionar(pila.desapilar())

        return " ".join(reversed(salida))

    def eval_expr_aritm(self) -> float:
        """Evalúa la expresión en notación prefija y retorna el resultado.

        Returns
        -------
        float
            El resultado de la expresión aritmética evaluada.
        """
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
