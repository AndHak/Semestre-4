
def expanded_form(num):
    largo = len(str(num))
    numeros = str(num)
    cadena = ""
    contador = 0
    agregar_mas = False

    while contador < largo:
        if numeros[contador] != "0":
            if agregar_mas:
                cadena += " + "
            numero = numeros[contador] + "0"*(largo-contador-1) 
            cadena += numero
            agregar_mas = True

        contador += 1

    return cadena

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))