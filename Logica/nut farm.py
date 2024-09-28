def shake_tree(tree):
    lista = [0] * len(tree[0])
    
    for index, nut in enumerate(tree[0]):
        if nut == "o":
            posicion = index
        else:
            continue

        for i, fila in enumerate(tree[1:], start=1):
            for j in range(len(fila)):
                if posicion is not None:
                    if fila[posicion] == "\\":
                        posicion += 1
                        break
                    elif fila[posicion] == "/":
                        posicion -= 1
                        break
                    elif fila[posicion] == "_":
                        posicion = None
                        break

        if posicion is not None:
            lista[posicion] += 1

    return lista
            