# Importar bibliotecas necesarias
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Datos ficticios: [tamaño, color]
# Tamaño: 0 = pequeño, 1 = mediano, 2 = grande
# Color: 0 = rojo, 1 = verde, 2 = amarillo
X = [[0, 0],  # Pequeño y rojo (manzana)
     [0, 1],  # Pequeño y verde (uva)
     [1, 0],  # Mediano y rojo (tomate)
     [1, 1],  # Mediano y verde (pepino)
     [2, 0],  # Grande y rojo (sandía)
     [2, 2]]  # Grande y amarillo (plátano)

# Etiquetas (clases): 0 = manzana, 1 = uva, 2 = tomate, 3 = pepino, 4 = sandía, 5 = plátano
y = [0, 1, 2, 3, 4, 5]

# Crear el modelo de árbol de decisión
modelo = DecisionTreeClassifier()

# Entrenar el modelo
modelo.fit(X, y)

# Visualizar el árbol de decisión
plt.figure(figsize=(10, 6))
tree.plot_tree(modelo, feature_names=["Tamaño", "Color"], class_names=["Manzana", "Uva", "Tomate", "Pepino", "Sandía", "Plátano"], filled=True)
plt.title("Árbol de Decisión para Clasificación de Frutas")
plt.show()
