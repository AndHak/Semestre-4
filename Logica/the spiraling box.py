def create_box(x, y):  ## m and n positive integers
    matriz = []
    for i in range(y):
        fila = []
        for j in range(x):
            #fila.append(j+1 if (j<x/2) else j if j == x/2 else x-j)
            dist_izquierda = j + 1
            dist_derecha = x - j
            dist_arriba = i + 1
            dist_abajo = y - i

            valor = dist_izquierda

            if dist_derecha < valor:
                valor = dist_derecha
            if dist_arriba < valor:
                valor = dist_arriba
            if dist_abajo < valor:
                valor = dist_abajo

            fila.append(valor)
        matriz.append(fila)
    return matriz

print(create_box(5, 8))
        
            
            