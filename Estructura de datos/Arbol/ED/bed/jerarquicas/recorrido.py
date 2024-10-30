# PRE-ORDEN
def pre_orden(arbol_bin):
    __pre_orden(arbol_bin.raiz)

def __pre_orden(sub_arbol):
    if sub_arbol:
        print(sub_arbol, False)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)

# CONSULTA #1
def str_pre_orden(arbol_bin, sep="|"):
    """Retorna una cadena en PRE-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[]' si corresponde a la raíz del árbol🌲
    - '()' si corresponde a un nodo rama🌿
    - '()' si corresponde a un nodo hoja🍂
    Ejemplo:
    ____50___ <--raiz
           /    \
       ___40    _60______
      /    \   /       \
     30    41 55     ___75___
    /  \        /        \
  25  35     65        _86
        /   \       /
       32  68    77
    '[]50|()40|()30|()25|()35|()32|()41|()60|()55|()75|()65|()68|()86|()77'🌲🌿🌿🍂🌿🍂🍂🌿🍂🌿🌿🍂🌿🍂
    """
    resultado = []
    __str_pre_orden(arbol_bin.raiz, resultado, sep, True)
    return sep.join(resultado)

def __str_pre_orden(sub_arbol, resultado, sep, es_raiz):
    if sub_arbol:
        tipo_nodo = "[🌲]{}" if es_raiz else "(🌿){}"
        if sub_arbol.izq is None and sub_arbol.der is None:
            tipo_nodo = "(🍂){}"  # Nodo hoja
        resultado.append(tipo_nodo.format(sub_arbol.clave))
        __str_pre_orden(sub_arbol.izq, resultado, sep, False)
        __str_pre_orden(sub_arbol.der, resultado, sep, False)

# IN-ORDEN
# CONSULTA #2
def in_orden(arbol_bin):
    __in_orden(arbol_bin.raiz)

def __in_orden(sub_arbol):
    if sub_arbol:
        __in_orden(sub_arbol.izq)
        print(sub_arbol.clave, end=" ")  # Imprime la clave
        __in_orden(sub_arbol.der)

# CONSULTA #3
def str_in_orden(arbol_bin, sep=":"):
    """Retorna una cadena en IN-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[]' si corresponde a la raíz del árbol🌲
    - '()' si corresponde a un nodo rama🌿
    - '()' si corresponde a un nodo hoja🍂
    Ejemplo:
    ____50___ <--raiz
           /    \
       ___40    _60______
      /    \   /       \
     30    41 55     ___75___
    /  \        /        \
  25  35     65        _86
        /   \       /
       32  68    77
    '()25:()30:()32:()35:()40:()41:[]50:()55:()60:()65:()68:()75:()77:()86'🍂🌿🍂🌿🌿🍂🌲🍂🌿🌿🍂🌿🍂🌿
    """
    resultado = []
    __str_in_orden(arbol_bin.raiz, resultado, sep, True)
    return sep.join(resultado)

def __str_in_orden(sub_arbol, resultado, sep, es_raiz):
    if sub_arbol:
        __str_in_orden(sub_arbol.izq, resultado, sep, False)
        tipo_nodo = "[🌲]{}" if es_raiz else "(🌿){}"
        if sub_arbol.izq is None and sub_arbol.der is None:
            tipo_nodo = "(🍂){}"  # Nodo hoja
        resultado.append(tipo_nodo.format(sub_arbol.clave))
        __str_in_orden(sub_arbol.der, resultado, sep, False)

# POST-ORDEN
# CONSULTA #4
def post_orden(arbol_bin):
    __post_orden(arbol_bin.raiz)

def __post_orden(sub_arbol):
    if sub_arbol:
        __post_orden(sub_arbol.izq)
        __post_orden(sub_arbol.der)
        print(sub_arbol.clave, end=" ")  # Imprime la clave

# CONSULTA #5
def str_post_orden(arbol_bin, sep="^"):
    """Retorna una cadena en POST-ORDEN, separando cada valor clave con 'sep',
    además identificar cada tipo de nodo con los siguientes emojis:
    - '[]' si corresponde a la raíz del árbol🌲
    - '()' si corresponde a un nodo rama🌿
    - '()' si corresponde a un nodo hoja🍂
    Ejemplo:
    ____50___ <--raiz
           /    \
       ___40    _60______
      /    \   /       \
     30    41 55     ___75___
    /  \        /        \
  25  35     65        _86
        /   \       /
       32  68    77
    '()25^()32^()35^()30^()41^()40^()55^()68^()65^()77^()86^()75^()60^[]50'🍂🍂🌿🌿🍂🌿🍂🍂🌿🍂🌿🌿🌿🌲
    """
    resultado = []
    __str_post_orden(arbol_bin.raiz, resultado, sep, True)
    return sep.join(resultado)

def __str_post_orden(sub_arbol, resultado, sep, es_raiz):
    if sub_arbol:
        __str_post_orden(sub_arbol.izq, resultado, sep, False)
        __str_post_orden(sub_arbol.der, resultado, sep, False)
        tipo_nodo = "[🌲]{}" if es_raiz else "(🌿){}"
        if sub_arbol.izq is None and sub_arbol.der is None:
            tipo_nodo = "(🍂){}"  # Nodo hoja
        resultado.append(tipo_nodo.format(sub_arbol.clave))
