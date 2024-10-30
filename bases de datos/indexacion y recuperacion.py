# Importamos las bibliotecas necesarias
import numpy as np  # Para trabajar con arreglos numéricos y realizar operaciones matemáticas
from sklearn.cluster import KMeans  # Algoritmo de clustering KMeans para agrupar imágenes similares
from PIL import Image  # Para abrir y procesar imágenes

# Definimos una clase que construirá un índice basado en el contenido de las imágenes
class IndiceContenidoImagen:
    
    def __init__(self, n_clusters=5):
        """
        Inicializa el índice con un número específico de clusters.
        El KMeans agrupará las imágenes en n_clusters grupos basándose en sus características.
        """
        self.kmeans = KMeans(n_clusters=n_clusters)  # Inicializamos KMeans con el número de clusters
        self.indice = {}  # Diccionario para almacenar las imágenes clasificadas por clúster
    
    def extraer_caracteristicas(self, ruta_imagen):
        """
        Dado el camino a una imagen, extraemos sus características en forma de arreglo numérico.
        Las características aquí son simplemente la representación RGB de los píxeles de la imagen.
        """
        img = Image.open(ruta_imagen).convert('RGB')  # Abrimos la imagen y la convertimos a formato RGB
        img_array = np.array(img)  # Convertimos la imagen a un arreglo NumPy (matriz de píxeles)
        caracteristicas = img_array.reshape(-1, 3)  # Reorganizamos la matriz en una sola dimensión (cada píxel es un vector de 3 elementos: R, G, B)
        return caracteristicas  # Retornamos las características (arreglo de píxeles)
    
    def construir_indice(self, rutas_imagenes):
        """
        Toma una lista de rutas de imágenes, extrae sus características y las agrupa usando KMeans.
        Crea un índice que agrupa las imágenes en clústeres según su contenido visual.
        """
        todas_caracteristicas = []  # Lista para almacenar las características de todas las imágenes
        
        # Recorremos todas las imágenes y extraemos sus características
        for ruta in rutas_imagenes:
            caracteristicas = self.extraer_caracteristicas(ruta)  # Extraemos características de la imagen actual
            todas_caracteristicas.append(caracteristicas)  # Añadimos las características a la lista
            
        # Convertimos la lista de características en un solo arreglo (pila vertical de matrices)
        todas_caracteristicas = np.vstack(todas_caracteristicas)
        
        # Entrenamos el modelo de KMeans usando todas las características recopiladas
        self.kmeans.fit(todas_caracteristicas)
        
        # Clasificamos las imágenes basándonos en los clústeres obtenidos por KMeans
        for ruta in rutas_imagenes:
            caracteristicas = self.extraer_caracteristicas(ruta)  # Extraemos características de cada imagen
            cluster = self.kmeans.predict(caracteristicas)[0]  # Predecimos a qué clúster pertenece la imagen (usamos el primer clúster encontrado)
            
            # Si el clúster aún no existe en el índice, lo inicializamos
            if cluster not in self.indice:
                self.indice[cluster] = []
                
            # Añadimos la ruta de la imagen al clúster correspondiente en el índice
            self.indice[cluster].append(ruta)
    
    def buscar(self, ruta_imagen_consulta):
        """
        Dada una imagen de consulta, busca las imágenes similares en el índice.
        """
        # Extraemos las características de la imagen de consulta
        caracteristicas_consulta = self.extraer_caracteristicas(ruta_imagen_consulta)
        
        # Predecimos a qué clúster pertenece la imagen de consulta
        cluster_consulta = self.kmeans.predict(caracteristicas_consulta)[0]
        
        # Retornamos las imágenes que pertenecen al mismo clúster que la imagen de consulta
        return self.indice.get(cluster_consulta, [])

# Uso del índice
indice = IndiceContenidoImagen(n_clusters=5)  # Creamos el índice con 5 clústeres (puede variar según necesidad)

# Rutas de ejemplo de imágenes
rutas_imagenes = ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg', ...]  # Lista de rutas de las imágenes

# Construimos el índice a partir de estas imágenes
indice.construir_indice(rutas_imagenes)

# Buscamos imágenes similares a una imagen de consulta
imagenes_similares = indice.buscar('imagen_consulta.jpg')

# Mostramos el resultado de imágenes similares encontradas
print("Imágenes similares:", imagenes_similares)
