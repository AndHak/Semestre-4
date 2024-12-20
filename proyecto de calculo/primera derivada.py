# Importar las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread('proyecto de calculo\edificio.jpg', cv2.IMREAD_GRAYSCALE)

# Obtenemos las dimensiones de la imagen asi:
alto, ancho = imagen.shape

#Creamos una matriz con ceros con el alto y el ancho de la imagen
#Usaremos esta matriz para almacenar las derivadas
derivada_x = np.zeros((alto, ancho))
derivada_y = np.zeros((alto, ancho))

#Calculaos la derivada en x usando la derivada hacia adelante
#Entramos a la fila de la imagen
for i in range(1, alto):
    #Entramos ahora en cada valor que hay en la fila, es decir los pixeles
    for j in range(1, ancho-1):
        #en la matriz con ceros en la posicion i, j
        #Vamos a poner el valor que este en la imagen aumentado en 1
        #restado con el pixel sin aumentar en 1
        derivada_x[i, j] = imagen[i, j+1] - imagen[i, j]

#Para calcular la derivada hacia adelante en y
#Es como si calcularamos la derivada hacia adelante con la imagen volteada
for i in range(1, alto-1):
    #Ahora restamos 1 a las filas para no salir del rango
    #Cuando aumentemos en este caso el pixel de abajo
    for j in range(1, ancho):
        #En la matriz con ceros en la posicion i, j
        #vamos a poner el valor que este en la imagen en esa posicion
        #restado con el pixel de abajo en este caso
        derivada_y[i, j] = imagen[i+1, j] - imagen[i, j]

derivada_xy = np.sqrt(derivada_x**2 + derivada_y**2)

# Primera fila: Imágenes originales y derivadas de primer orden
plt.subplot(2, 4, 1)
plt.imshow(imagen, cmap="gray")
plt.title("Imagen original")

plt.subplot(2, 4, 2)
plt.imshow(derivada_x, cmap="gray")
plt.title("Derivada hacia adelante en X")

plt.subplot(2, 4, 3)
plt.imshow(derivada_y, cmap="gray")
plt.title("Derivada hacia adelante en Y")

plt.subplot(2, 4, 4)
plt.imshow(derivada_xy, cmap="gray")
plt.title("Derivadas X e Y Juntas")

plt.show()
