from arbol_decision import ArbolDecision

def main():
    arbol = ArbolDecision()
    
    # Agregar el primer nodo (raíz) sin nodo padre
    arbol.agregar_nodo(None, "edad", "Menor de 18 años", es_hoja=True, clasificacion="Niño")
    
    # Agregar más nodos con un nodo padre específico (usando la raíz como nodo padre)
    raiz = arbol.raiz
    arbol.agregar_nodo(raiz, "edad", "18 a 30 años", es_hoja=True, clasificacion="Adulto Joven")
    arbol.agregar_nodo(raiz, "edad", "31 a 40 años", es_hoja=True, clasificacion="Adulto")
    arbol.agregar_nodo(raiz, "edad", "41 a 50 años", es_hoja=True, clasificacion="Adulto")
    arbol.agregar_nodo(raiz, "edad", "Más de 50 años", es_hoja=True, clasificacion="Adulto Mayor")
    
    # Agregar más nodos de clasificación según la ocupación
    nodo_adulto_joven = raiz.hijos[0]  # Nodo "18 a 30 años"
    arbol.agregar_nodo(nodo_adulto_joven, "ocupacion", "Estudiante", es_hoja=True, clasificacion="Estudiante")
    arbol.agregar_nodo(nodo_adulto_joven, "ocupacion", "Trabajador", es_hoja=True, clasificacion="Trabajador")
    
    nodo_adulto = raiz.hijos[1]  # Nodo "31 a 40 años"
    arbol.agregar_nodo(nodo_adulto, "ocupacion", "Trabajador", es_hoja=True, clasificacion="Trabajador")
    
    nodo_adulto_mayor = raiz.hijos[3]  # Nodo "Más de 50 años"
    arbol.agregar_nodo(nodo_adulto_mayor, "ocupacion", "Jubilado", es_hoja=True, clasificacion="Jubilado")
    
    # Agregar nodo de ocupación para el rango de 41 a 50 años
    nodo_adulto_mayor_2 = raiz.hijos[2]  # Nodo "41 a 50 años"
    arbol.agregar_nodo(nodo_adulto_mayor_2, "ocupacion", "Trabajador", es_hoja=True, clasificacion="Trabajador")
    
    # Guardar el árbol en un archivo JSON
    arbol.guardar_datos("arbol_decision.json")

if __name__ == "__main__":
    main()