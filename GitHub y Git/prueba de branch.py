print("Este es un codigo interesante")

import random

numero = input("Escoje un numero del 1 al 5")

random_number = random.randint(1,5)

if int(numero) == random_number:
    print(f"Ganaste, el numero oculto era el {random_number}")
else:
    print(f"Perdiste, el numero oculto era {random_number}")