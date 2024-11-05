from bed.jerarquicas.excepciones import DuplicatedKeyError, HomogeneityError
from bed.jerarquicas.nodos import *
from bed.jerarquicas.arbol_desicion import ArbolDecision


def test_arbol_decision_edades():
    # Crear el árbol de decisión
    arbol = ArbolDecision()
    
    # Adicionar nodos de decisión en forma de rango
    arbol.adicionar(13, "Niño", es_hoja=False)        # Menores de 13
    arbol.adicionar(17, "Adolescente", es_hoja=False) # Entre 13 y 17
    arbol.adicionar(35, "Adulto Joven", es_hoja=False)# Entre 18 y 35
    arbol.adicionar(100, "Adulto Mayor", es_hoja=True)# Mayor o igual a 36
    
    # Definir ramas para cada nodo, para clarificar los intervalos
    arbol.nodo_izq(13, "Niño")  # Para edades menores a 13
    arbol.nodo_der(13, 17)      # Edad entre 13 y 17
    arbol.nodo_der(17, 35)      # Edad entre 18 y 35
    arbol.nodo_der(35, "Adulto Mayor") # Para edades de 36 en adelante

    # Realizar evaluaciones en el árbol
    print("Clasificación de edades en el árbol de decisión:")
    edades = [5, 15, 20, 40, 70]
    resultados_esperados = ["Niño", "Adolescente", "Adulto Joven", "Adulto Mayor", "Adulto Mayor"]

    for edad, esperado in zip(edades, resultados_esperados):
        resultado = arbol.evaluar(edad)
        assert resultado == esperado, f"Error: edad {edad} clasificada como {resultado}, esperaba {esperado}"
        print(f"Edad {edad}: {resultado} (esperado: {esperado})")

# Ejecutar el test
test_arbol_decision_edades()
