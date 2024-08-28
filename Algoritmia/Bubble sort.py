import time
import numpy as np

# Crear el array original
original_A = np.random.rand(5000)

# Ordenamiento con np.sort
A = np.copy(original_A)  # Copia para mantener el array original intacto
tic = time.time()
B = np.sort(A)
toc = time.time()
print(f"Tiempo de ordenamiento con np.sort: {1000*(toc-tic):.2f} ms")

# Ordenamiento burbuja
A = np.copy(original_A)  # Copia para mantener el array original intacto
tic = time.time()
for i in range(len(A)):
    for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
toc = time.time()
print(f"Tiempo de ordenamiento burbuja: {1000*(toc-tic):.2f} ms")

# Ordenamiento burbuja con lista
A = np.copy(original_A).tolist()  # Convertir a lista para la prueba
tic = time.time()
for i in range(len(A)):
    for j in range(len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
toc = time.time()
A = np.array(A)  # Convertir de vuelta a array para consistencia
print(f"Tiempo de ordenamiento burbuja con lista: {1000*(toc-tic):.2f} ms")

# Ordenamiento burbuja mejorado
A = np.copy(original_A)  # Copia para mantener el array original intacto
tic = time.time()
i = 0
control = True
while (i <= len(A) - 2) and control:
    control = False
    for j in range(0, len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            control = True
    i += 1
toc = time.time()
print(f"Tiempo de ordenamiento burbuja mejorado: {1000*(toc-tic):.2f} ms")

# Ordenamiento burbuja mejorado con lista
A = np.copy(original_A).tolist()  # Convertir a lista para la prueba
tic = time.time()
i = 0
control = True
while (i <= len(A) - 2) and control:
    control = False
    for j in range(0, len(A) - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            control = True
    i += 1
toc = time.time()
A = np.array(A)  # Convertir de vuelta a array para consistencia
print(f"Tiempo de ordenamiento burbuja mejorado con lista: {1000*(toc-tic):.2f} ms")
