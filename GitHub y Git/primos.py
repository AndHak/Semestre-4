def es_primo(num):
    """Función para verificar si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calcular_primo():
    """Función principal para verificar números primos y fibonaccis."""
    numeros = True
    while numeros:
        try:
            numero = input("Digite un número o 'Q' para salir: ")
            if numero.upper() == "Q":
                numeros = False
            elif es_primo(int(numero)):
                print("El número es primo.")
            elif es_fibonacci(int(numero)):
                print("Este numero es fibonacci")
            else:
                print("Este número no es primo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("Programa finalizado.")

calcular_primo()
