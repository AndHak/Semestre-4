import json  
import os 


if __package__:
    from bed.jerarquicas.nodo_decision import NodoDecision  
    from bed.jerarquicas.excepciones import NodoNoEncontradoError, ArbolVacioError, NodoYaExisteError 
else:  
    from nodo_decision import NodoDecision  
    from excepciones import NodoNoEncontradoError, ArbolVacioError, NodoYaExisteError  


class ArbolDecision:
    def __init__(self):  # Método de inicialización
        # Inicializa el árbol con un nodo raíz vacío
        self.raiz = NodoDecision("raiz", "Inicio")  # Crea el nodo raíz del árbol con "criterio" como "raiz" y "valor" como "Inicio"

    # Método para agregar un nodo al árbol de decisiones
    def agregar_nodo(self, nodo_padre, criterio, valor, es_hoja=False, clasificacion=None):
        # Crea una instancia de NodoDecision con los parámetros dados
        nuevo_nodo = NodoDecision(criterio, valor, es_hoja=es_hoja, clasificacion=clasificacion)

        if self.raiz is None:  # Si el árbol está vacío, asigna el nodo creado como la raíz
            self.raiz = nuevo_nodo
        elif nodo_padre:  # Si se proporciona un nodo padre
            nodo_padre.hijos.append(nuevo_nodo)  # Agrega el nuevo nodo como hijo del nodo padre

    # Busca un nodo existente o crea uno nuevo en el nodo especificado
    def buscar_o_crear_nodo(self, nodo, criterio, valor):
        # Itera sobre los hijos del nodo para buscar uno que coincida con el criterio y el valor
        for hijo in nodo.hijos:
            if hijo.criterio == criterio and hijo.valor == valor:  # Si encuentra coincidencia, devuelve el hijo existente
                return hijo
        # Si no existe un nodo coincidente, crea uno nuevo
        nuevo_nodo = NodoDecision(criterio, valor)  # Crea un nuevo nodo con el criterio y valor dados
        nodo.hijos.append(nuevo_nodo)  # Agrega el nuevo nodo a la lista de hijos del nodo actual
        return nuevo_nodo  # Devuelve el nuevo nodo

    # Agrega nodos al árbol según los criterios de edad y ocupación
    def agregar_por_criterios(self, edad, ocupacion, clasificacion):
        nodo_edad = self._agregar_por_edad(edad)  # Crea o recupera un nodo para el rango de edad correspondiente
        nodo_ocupacion = self.buscar_o_crear_nodo(nodo_edad, "ocupacion", ocupacion)  # Crea o recupera un nodo para la ocupación
        nodo_ocupacion.es_hoja = True  # Marca el nodo de ocupación como hoja
        nodo_ocupacion.clasificacion = clasificacion  # Asigna la clasificación al nodo de ocupación

    # Define el rango de edad y busca o crea el nodo correspondiente
    def _agregar_por_edad(self, edad):
        if edad < 18:  # Determina el rango de edad según el valor de edad
            rango_edad = "Menor de 18"
        elif 18 <= edad <= 30:
            rango_edad = "18 a 30"
        elif 31 <= edad <= 50:
            rango_edad = "31 a 50"
        else:
            rango_edad = "Mayor de 50"

        return self.buscar_o_crear_nodo(self.raiz, "edad", rango_edad)  # Devuelve el nodo correspondiente al rango de edad

    # Guarda el árbol de decisión en un archivo JSON
    def guardar_datos(self, archivo_nombre="arbol_decision.json"):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta del archivo actual
        ruta_completa = os.path.join(ruta_actual, archivo_nombre)  # Crea la ruta completa para el archivo JSON
        
        with open(ruta_completa, 'w') as f:  # Abre el archivo en modo escritura
            # Escribe la estructura del árbol en formato JSON
            json.dump(self._nodo_a_diccionario(self.raiz), f, indent=4)
            print(f"Árbol guardado en '{ruta_completa}'.")  # Imprime un mensaje de confirmación

    # Convierte un nodo en un diccionario para que sea compatible con JSON
    def _nodo_a_diccionario(self, nodo):
        if not nodo:  # Si el nodo es None, retorna None
            return None
        # Retorna un diccionario con la estructura del nodo y sus hijos
        return {
            "criterio": nodo.criterio,  # Criterio del nodo
            "valor": nodo.valor,  # Valor del nodo
            "es_hoja": nodo.es_hoja,  # Indica si el nodo es una hoja
            "clasificacion": nodo.clasificacion,  # Clasificación del nodo, si es hoja
            "hijos": [self._nodo_a_diccionario(hijo) for hijo in nodo.hijos] if nodo.hijos else []  # Lista de hijos en formato de diccionario
        }
