# Importamos las bibliotecas necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos Iris
data = load_iris()
X = data.data  # Características (longitud y ancho de sépalos y pétalos)
y = data.target  # Etiquetas (tipos de flores)

# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos el clasificador de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenamos el modelo con los datos de entrenamiento
clf.fit(X_train, y_train)

# Realizamos predicciones sobre los datos de prueba
y_pred = clf.predict(X_test)

# Calculamos y mostramos la precisión del modelo
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del árbol de decisión: {precision * 100:.2f}%")

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Graficamos el árbol de decisión
plt.figure(figsize=(12,8))
plot_tree(clf, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.show()
