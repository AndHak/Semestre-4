from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QPushButton, 
    QVBoxLayout, QWidget, QGraphicsEllipseItem, QGraphicsTextItem, QInputDialog, 
    QMessageBox, QTableWidget, QTableWidgetItem, QDockWidget, QLabel, QDialog, 
    QComboBox, QSpinBox, QFormLayout, QDialogButtonBox
)
from PySide6.QtGui import QPen, QBrush, QCursor, QFont, QPainter
from PySide6.QtCore import Qt


class ConectarNodosDialog(QDialog):
    def __init__(self, nombres_nodos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Conectar Nodos")

        # Campos de entrada
        self.origen_combo = QComboBox()
        self.origen_combo.addItems(nombres_nodos)

        self.destino_combo = QComboBox()
        self.destino_combo.addItems(nombres_nodos)
        self.destino_combo.setCurrentIndex(1)  # Para evitar que origen y destino sean iguales inicialmente

        self.peso_spinbox = QSpinBox()
        self.peso_spinbox.setRange(1, 100)
        self.peso_spinbox.setValue(1)

        # Layout
        layout = QFormLayout()
        layout.addRow("Nodo de Origen:", self.origen_combo)
        layout.addRow("Nodo de Destino:", self.destino_combo)
        layout.addRow("Peso:", self.peso_spinbox)

        # Botones
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

        self.setLayout(layout)

    def get_result(self):
        return (
            self.origen_combo.currentText(),
            self.destino_combo.currentText(),
            self.peso_spinbox.value()
        )


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
        self.setGeometry(100, 100, 1000, 600)

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

        # Dock para la tabla y el costo total
        self.dock = QDockWidget("Resultados del MST", self)
        self.dock.setAllowedAreas(Qt.RightDockWidgetArea)
        self.tabla_mst = QTableWidget(0, 3)
        self.tabla_mst.setHorizontalHeaderLabels(["Origen", "Destino", "Peso"])
        self.costo_total_label = QLabel("Costo Total: 0")
        dock_layout = QVBoxLayout()
        dock_layout.addWidget(self.tabla_mst)
        dock_layout.addWidget(self.costo_total_label)
        dock_widget = QWidget()
        dock_widget.setLayout(dock_layout)
        self.dock.setWidget(dock_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # Conexiones
        self.boton_agregar_nodo.clicked.connect(self.modo_agregar_nodo)
        self.boton_eliminar_nodo.clicked.connect(self.modo_eliminar_nodo)
        self.boton_conectar_nodo.clicked.connect(self.modo_conectar_nodo)
        self.boton_calcular_mst.clicked.connect(self.calcular_mst)

        self.nodos = []
        self.aristas = []

    def modo_agregar_nodo(self):
        nombre, ok = QInputDialog.getText(self, "Crear Nodo", "Nombre del Nodo:")
        if ok and nombre:
            if any(nodo.nombre == nombre for nodo in self.nodos):
                QMessageBox.warning(self, "Error", "Ya existe un nodo con ese nombre.")
                return

            posicion = self.vista.mapToScene(self.vista.mapFromGlobal(QCursor.pos()))
            nodo = Nodo(posicion.x(), posicion.y(), nombre, self.escena)
            self.nodos.append(nodo)

    def modo_eliminar_nodo(self):
        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        nombre, ok = QInputDialog.getItem(self, "Eliminar Nodo", "Seleccione un Nodo:", nombres_nodos, editable=False)

        if ok and nombre:
            nodo = next(n for n in self.nodos if n.nombre == nombre)
            nodo.eliminar(self.escena)
            self.nodos.remove(nodo)

    def modo_conectar_nodo(self):
        if len(self.nodos) < 2:
            QMessageBox.warning(self, "Error", "Se necesitan al menos 2 nodos para conectar.")
            return

        dialog = ConectarNodosDialog([nodo.nombre for nodo in self.nodos], self)
        
        # Actualizar opciones dinámicas
        dialog.origen_combo.currentIndexChanged.connect(
            lambda: dialog.destino_combo.clear() or dialog.destino_combo.addItems(
                [n.nombre for n in self.nodos if n.nombre != dialog.origen_combo.currentText()]
            )
        )

        if dialog.exec():
            origen_nombre, destino_nombre, peso = dialog.get_result()

            if origen_nombre == destino_nombre:
                QMessageBox.warning(self, "Error", "El origen y el destino no pueden ser iguales.")
                return

            origen = next(n for n in self.nodos if n.nombre == origen_nombre)
            destino = next(n for n in self.nodos if n.nombre == destino_nombre)

            # Verificar si la conexión ya existe
            for arista in self.aristas:
                if (arista.origen == origen and arista.destino == destino) or \
                (arista.origen == destino and arista.destino == origen):
                    arista.peso = peso
                    arista.setPlainText(str(peso))
                    arista.ajustar()
                    return

            # Crear nueva conexión
            arista = Arista(origen, destino, peso, self.escena)
            origen.add_arista(arista)
            destino.add_arista(arista)
            self.aristas.append(arista)

    def calcular_mst(self):
        """Calcular y mostrar el árbol de expansión mínima (MST)."""
        if len(self.nodos) < 2:
            QMessageBox.warning(self, "Error", "Se necesitan al menos 2 nodos para calcular el MST.")
            return

        # Restaurar el color de todas las aristas
        for arista in self.aristas:
            arista.linea.setPen(QPen(Qt.black, 2))

        # Algoritmo de Kruskal
        edges = sorted([(arista.peso, arista.origen.nombre, arista.destino.nombre, arista) for arista in self.aristas])
        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for nodo in self.nodos:
            parent[nodo.nombre] = nodo.nombre
            rank[nodo.nombre] = 0

        mst = []
        costo_total = 0
        for peso, origen, destino, arista in edges:
            if find(origen) != find(destino):
                union(origen, destino)
                mst.append((origen, destino, peso, arista))
                costo_total += peso

        # Colorear aristas del MST en rojo
        for _, _, _, arista in mst:
            arista.linea.setPen(QPen(Qt.red, 2))

        # Actualizar tabla y costo total
        self.tabla_mst.setRowCount(0)
        for origen, destino, peso, _ in mst:
            fila = self.tabla_mst.rowCount()
            self.tabla_mst.insertRow(fila)
            self.tabla_mst.setItem(fila, 0, QTableWidgetItem(origen))
            self.tabla_mst.setItem(fila, 1, QTableWidgetItem(destino))
            self.tabla_mst.setItem(fila, 2, QTableWidgetItem(str(peso)))

        self.costo_total_label.setText(f"Costo Total: {costo_total}")



if __name__ == "__main__":
    app = QApplication()
    ventana = AplicacionGrafo()
    ventana.show()
    app.exec()
