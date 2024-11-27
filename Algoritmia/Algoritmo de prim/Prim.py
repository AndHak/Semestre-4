
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene,
    QPushButton, QVBoxLayout, QWidget, QGraphicsEllipseItem,
    QGraphicsTextItem, QInputDialog, QMessageBox, QTableWidget,
    QTableWidgetItem
)
from PySide6.QtGui import QPen, QBrush, QCursor, QFont, QPainter
from PySide6.QtCore import Qt


class Arista(QGraphicsTextItem):
    def __init__(self, origen, destino, peso, escena):
        super().__init__()
        self.origen = origen
        self.destino = destino
        self.peso = peso

        # Línea de la arista
        self.linea = escena.addLine(0, 0, 0, 0, QPen(Qt.black, 2))
        self.ajustar()

        # Peso de la arista
        self.setPlainText(str(peso))
        self.setDefaultTextColor(Qt.black)
        fuente = QFont("Arial", 12, QFont.Bold)
        self.setFont(fuente)

        self.escena = escena
        self.escena.addItem(self)

    def ajustar(self):
        """Ajustar la línea y posición del peso según los nodos conectados."""
        origen = self.origen.sceneBoundingRect().center()
        destino = self.destino.sceneBoundingRect().center()
        self.linea.setLine(origen.x(), origen.y(), destino.x(), destino.y())
        punto_medio = self.linea.line().pointAt(0.5)
        self.setPos(punto_medio.x(), punto_medio.y())

    def eliminar(self):
        """Eliminar la arista de la escena."""
        self.escena.removeItem(self.linea)
        self.escena.removeItem(self)


class Nodo(QGraphicsEllipseItem):
    def __init__(self, x, y, nombre, escena):
        super().__init__(-30, -30, 60, 60)
        self.setBrush(QBrush(Qt.yellow))
        self.setPen(QPen(Qt.black, 2))
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable)
        self.setZValue(1)
        self.nombre = nombre
        self.aristas = []

        # Texto del nodo
        self.texto = QGraphicsTextItem(nombre, self)
        self.texto.setDefaultTextColor(Qt.black)
        fuente = QFont("Arial", 14, QFont.Bold)
        self.texto.setFont(fuente)
        self.texto.setPos(-self.texto.boundingRect().width() / 2, -20)
        escena.addItem(self)
        self.setPos(x, y)

    def add_arista(self, arista):
        self.aristas.append(arista)

    def eliminar_arista(self, arista):
        if arista in self.aristas:
            self.aristas.remove(arista)

    def mouseMoveEvent(self, event):
        """Actualizar las aristas conectadas al mover el nodo."""
        super().mouseMoveEvent(event)
        for arista in self.aristas:
            arista.ajustar()

    def eliminar(self, escena):
        """Eliminar nodo y sus aristas asociadas."""
        while self.aristas:
            arista = self.aristas.pop()
            arista.eliminar()
        escena.removeItem(self)


class AplicacionGrafo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Grafos")
        self.setGeometry(100, 100, 800, 600)

        self.escena = QGraphicsScene()
        self.vista = QGraphicsView(self.escena)
        self.vista.setRenderHint(QPainter.Antialiasing)

        # Botones
        self.boton_agregar_nodo = QPushButton("Crear Nodo")
        self.boton_eliminar_nodo = QPushButton("Eliminar Nodo")
        self.boton_conectar_nodo = QPushButton("Conectar Nodos")
        self.boton_calcular_mst = QPushButton("Calcular MST")

        layout = QVBoxLayout()
        layout.addWidget(self.vista)
        layout.addWidget(self.boton_agregar_nodo)
        layout.addWidget(self.boton_eliminar_nodo)
        layout.addWidget(self.boton_conectar_nodo)
        layout.addWidget(self.boton_calcular_mst)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Conexiones
        self.boton_agregar_nodo.clicked.connect(self.modo_agregar_nodo)
        self.boton_eliminar_nodo.clicked.connect(self.modo_eliminar_nodo)
        self.boton_conectar_nodo.clicked.connect(self.modo_conectar_nodo)
        self.boton_calcular_mst.clicked.connect(self.calcular_mst)

        self.nodos = []
        self.aristas = []

    def modo_agregar_nodo(self):
        """Agregar un nodo a la escena."""
        nombre, ok = QInputDialog.getText(self, "Crear Nodo", "Nombre del Nodo:")
        if ok and nombre:
            if any(nodo.nombre == nombre for nodo in self.nodos):
                QMessageBox.warning(self, "Error", "Ya existe un nodo con ese nombre.")
                return  # Evitar duplicados

            posicion = self.vista.mapToScene(self.vista.mapFromGlobal(QCursor.pos()))
            nodo = Nodo(posicion.x(), posicion.y(), nombre, self.escena)
            self.nodos.append(nodo)

    def modo_eliminar_nodo(self):
        """Eliminar un nodo seleccionado."""
        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        nombre, ok = QInputDialog.getItem(self, "Eliminar Nodo", "Seleccione un Nodo:", nombres_nodos, editable=False)

        if ok and nombre:
            nodo = next(n for n in self.nodos if n.nombre == nombre)
            nodo.eliminar(self.escena)
            self.nodos.remove(nodo)

    def modo_conectar_nodo(self):
        """Conectar dos nodos."""
        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        origen_nombre, ok = QInputDialog.getItem(self, "Conectar Nodos", "Nodo de Origen:", nombres_nodos, editable=False)
        if not ok:
            return
        destino_nombre, ok = QInputDialog.getItem(self, "Conectar Nodos", "Nodo de Destino:", nombres_nodos, editable=False)
        if not ok:
            return
        peso, ok = QInputDialog.getInt(self, "Peso de la Arista", "Ingrese el peso:")
        if not ok:
            return

        origen = next(n for n in self.nodos if n.nombre == origen_nombre)
        destino = next(n for n in self.nodos if n.nombre == destino_nombre)

        arista = Arista(origen, destino, peso, self.escena)
        self.aristas.append(arista)
        origen.add_arista(arista)
        destino.add_arista(arista)

    def calcular_mst(self):
        """Calcular el MST con el algoritmo de Prim y mostrar la tabla de resultados."""
        if not self.nodos or not self.aristas:
            QMessageBox.warning(self, "Error", "No hay nodos o aristas en el grafo.")
            return

        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        nodo_inicial, ok = QInputDialog.getItem(self, "Calcular MST", "Seleccione el Nodo Inicial:", nombres_nodos, editable=False)
        if not ok:
            return

        # Algoritmo de Prim
        nodo_inicio = next(n for n in self.nodos if n.nombre == nodo_inicial)
        visitados = {nodo_inicio}
        aristas_posibles = list(nodo_inicio.aristas)
        mst_aristas = []
        total_costo = 0

        while aristas_posibles:
            aristas_posibles.sort(key=lambda e: e.peso)
            arista_minima = aristas_posibles.pop(0)
            siguiente_nodo = arista_minima.destino if arista_minima.origen in visitados else arista_minima.origen

            if siguiente_nodo not in visitados:
                visitados.add(siguiente_nodo)
                mst_aristas.append(arista_minima)
                total_costo += arista_minima.peso
                for arista in siguiente_nodo.aristas:
                    if arista.destino not in visitados or arista.origen not in visitados:
                        aristas_posibles.append(arista)

        # Mostrar tabla con nodos y costos
        self.mostrar_resultados_mst(mst_aristas, total_costo)

    def calcular_mst(self):
        """Calcular el MST con el algoritmo de Prim, permitiendo elegir el nodo inicial."""
        if not self.nodos or not self.aristas:
            return

        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        nodo_inicial, ok = QInputDialog.getItem(self, "Calcular MST", "Seleccione el Nodo Inicial:", nombres_nodos, editable=False)
        if not ok:
            return

        # Algoritmo de Prim
        nodo_inicio = next(n for n in self.nodos if n.nombre == nodo_inicial)
        visitados = {nodo_inicio}
        aristas_posibles = list(nodo_inicio.aristas)
        mst_aristas = []

        while aristas_posibles:
            aristas_posibles.sort(key=lambda e: e.peso)
            arista_minima = aristas_posibles.pop(0)
            siguiente_nodo = arista_minima.destino if arista_minima.origen in visitados else arista_minima.origen

            if siguiente_nodo not in visitados:
                visitados.add(siguiente_nodo)
                mst_aristas.append(arista_minima)
                for arista in siguiente_nodo.aristas:
                    if arista.destino not in visitados or arista.origen not in visitados:
                        aristas_posibles.append(arista)

        # Mostrar MST
        for arista in mst_aristas:
            arista.linea.setPen(QPen(Qt.red, 3))


if __name__ == "__main__":
    app = QApplication([])
    ventana = AplicacionGrafo()
    ventana.show()
    app.exec()
