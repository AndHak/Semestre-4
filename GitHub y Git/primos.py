def es_primo(num):
    """Función para verificar si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def calcular_primo():
    """Función principal para verificar números primos."""
    primos = True
    while primos:
        try:
            primo = input("Digite un número o 'Q' para salir: ")
            if primo.upper() == "Q":
                primos = False
            elif es_primo(int(primo)):
                print("El número es primo.")
            else:
                print("Este número no es primo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("Programa finalizado.")

calcular_primo()
