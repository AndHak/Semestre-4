from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene,
    QPushButton, QVBoxLayout, QWidget, QGraphicsEllipseItem,
    QGraphicsTextItem, QInputDialog, QMessageBox, QTableWidget,
)
from PySide6.QtGui import QPen, QBrush, QCursor, QFont, QPainter, QStandardItem, QStandardItemModel, QColor, QRadialGradient
from PySide6.QtCore import Qt
from ui_MainApp import Ui_MainWindow

class Nodo(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, x, y, nombre, escena):
        super().__init__(-30, -30, 60, 60)

        # Estilo con degradado
        gradiente = QRadialGradient(0, 0, 40)
        gradiente.setColorAt(0, QColor(207, 227, 241))
        gradiente.setColorAt(1, QColor(62, 160, 227))
        self.setBrush(QBrush(gradiente))
        self.setPen(QPen(Qt.black, 2))

        # Movilidad y selección
        self.setFlag(QtWidgets.QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable)
        self.setZValue(1)

        self.nombre = nombre
        self.aristas = []

        # Texto del nodo
        self.texto = QtWidgets.QGraphicsTextItem(nombre, self)
        self.texto.setDefaultTextColor(Qt.black)
        fuente = QFont("Arial", 14, QFont.Bold)
        self.texto.setFont(fuente)
        self.texto.setPos(-self.texto.boundingRect().width() / 2, -15)

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

    def eliminar(self, escena, aristas_globales):
        """Eliminar nodo y sus aristas asociadas."""
        while self.aristas:
            arista = self.aristas.pop()
            # Eliminar la arista de la escena y de los nodos conectados
            arista.origen.eliminar_arista(arista)
            arista.destino.eliminar_arista(arista)
            arista.eliminar()
            
            # Eliminar también de la lista global de aristas si existe
            if arista in aristas_globales:
                aristas_globales.remove(arista)

        # Finalmente, eliminar el nodo de la escena
        escena.removeItem(self)



class Arista(QGraphicsTextItem):
    def __init__(self, origen, destino, peso, escena):
        super().__init__()
        self.origen = origen
        self.destino = destino
        self.peso = peso

        # Línea de la arista
        self.linea = escena.addLine(0, 0, 0, 0, QPen(Qt.darkGray, 2))
        self.ajustar()

        # Peso de la arista
        self.setPlainText(str(peso))
        self.setDefaultTextColor(Qt.darkBlue)
        fuente = QFont("Arial", 10, QFont.Bold)
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


class ConectarNodosDialog(QtWidgets.QDialog):
    def __init__(self, nombres_nodos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Conectar Nodos")

        # Campos de entrada
        layout = QtWidgets.QFormLayout()

        self.origen_combo = QtWidgets.QComboBox()
        self.origen_combo.addItems(nombres_nodos)

        self.destino_combo = QtWidgets.QComboBox()
        self.destino_combo.addItems(nombres_nodos)

        # Validación para evitar seleccionar el mismo nodo
        self.origen_combo.currentIndexChanged.connect(self.actualizar_destino)
        
        self.peso_spinbox = QtWidgets.QSpinBox()
        self.peso_spinbox.setRange(1, 1000)  # Rango de peso más amplio
        self.peso_spinbox.setValue(1)

        layout.addRow("Nodo de Origen:", self.origen_combo)
        layout.addRow("Nodo de Destino:", self.destino_combo)
        layout.addRow("Peso:", self.peso_spinbox)

        # Botones
        botones = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)
        layout.addWidget(botones)

        self.setLayout(layout)
        
        # Inicializar combinación de destinos
        self.actualizar_destino()

    def actualizar_destino(self):
        # Deshabilitar el nodo de origen en la lista de destino
        origen_actual = self.origen_combo.currentText()
        
        # Guardar el destino actual
        destino_actual = self.destino_combo.currentText()
        
        # Limpiar y repoblar el combo de destino
        self.destino_combo.clear()
        destinos_disponibles = [
            nodo for nodo in [self.origen_combo.itemText(i) for i in range(self.origen_combo.count())] 
            if nodo != origen_actual
        ]
        self.destino_combo.addItems(destinos_disponibles)
        
        # Intentar mantener el destino anterior si está disponible
        index = self.destino_combo.findText(destino_actual)
        if index != -1:
            self.destino_combo.setCurrentIndex(index)

    def get_result(self):
        return (
            self.origen_combo.currentText(),
            self.destino_combo.currentText(),
            self.peso_spinbox.value()
        )


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup UI from designer file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Algoritmo de Prim")
        self.setWindowIcon(QtGui.QIcon("C:\Programacion Universidad\Semestre 4\Algoritmia\Algoritmo de prim\icons\icons8-algorithm-100.png"))
        

        # Crear la escena gráfica
        self.escena = QGraphicsScene()
        self.vista = QGraphicsView(self.escena)
        self.vista.setRenderHint(QPainter.Antialiasing)

        # Busca el layout existente y reemplaza su contenido
        layout = self.ui.widget_grafo.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.widget_grafo)
        
        # Limpiar layout existente
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Agregar la vista al layout
        layout.addWidget(self.vista)

        # Configuraciones adicionales
        self.nodos = []
        self.aristas = []

        # Conectar botones
        self.ui.add_nodo_button.clicked.connect(self.modo_agregar_nodo)
        self.ui.delete_nodo_button.clicked.connect(self.modo_eliminar_nodo)
        self.ui.hacer_enlace_button.clicked.connect(self.modo_conectar_nodo)
        self.ui.delete_link.clicked.connect(self.modo_eliminar_enlace)
        self.ui.delete_all_button.clicked.connect(self.eliminar_todo)
        self.ui.calcular_mst_button.clicked.connect(self.calcular_mst)

    def modo_eliminar_enlace(self):
        """Eliminar un enlace específico entre dos nodos."""
        # Primero, verificar si hay aristas
        if not self.aristas:
            QMessageBox.information(self, "Error", "No hay enlaces para eliminar.")
            return

        # Crear lista de enlaces para mostrar
        enlaces = [f"{arista.origen.nombre} --> {arista.destino.nombre} (Peso: {arista.peso})" for arista in self.aristas]
        
        # Mostrar diálogo de selección de enlace
        enlace_seleccionado, ok = QInputDialog.getItem(
            self, 
            "Eliminar Enlace", 
            "Seleccione el enlace a eliminar:", 
            enlaces, 
            editable=False
        )

        if ok and enlace_seleccionado:
            # Encontrar la arista correspondiente
            for arista in self.aristas[:]:  # Copia de lista para seguridad al modificar
                if (f"{arista.origen.nombre} --> {arista.destino.nombre} (Peso: {arista.peso})" == enlace_seleccionado):
                    # Eliminar la arista de los nodos
                    arista.origen.eliminar_arista(arista)
                    arista.destino.eliminar_arista(arista)
                    
                    # Eliminar la arista de la escena
                    arista.eliminar()
                    
                    # Eliminar de la lista de aristas
                    self.aristas.remove(arista)
                    
                    break


    def eliminar_todo(self):
        """Eliminar todos los nodos y aristas."""
        # Eliminar todos los nodos
        while self.nodos:
            nodo = self.nodos.pop()
            nodo.eliminar(self.escena)


        self.aristas.clear()
        self.ui.tableview_mst.setModel(None)
        self.ui.label_digitar_costo_total.setText(" 0")


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
        if not self.nodos:
            QMessageBox.information(self, "Error", "No hay nodos para eliminar.")
            return

        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        nombre, ok = QInputDialog.getItem(self, "Eliminar Nodo", "Seleccione un Nodo:", nombres_nodos, editable=False)

        if ok and nombre:
            nodo = next(n for n in self.nodos if n.nombre == nombre)
            nodo.eliminar(self.escena, self.aristas)
            self.nodos.remove(nodo)

    def modo_conectar_nodo(self):
        """Conectar dos nodos."""
        if len(self.nodos) < 2:
            QMessageBox.information(self, "Error", "Debe tener al menos 2 nodos para crear una conexión.")
            return

        nombres_nodos = [nodo.nombre for nodo in self.nodos]
        dialogo = ConectarNodosDialog(nombres_nodos, self)

        if dialogo.exec() == QtWidgets.QDialog.Accepted:
            origen_nombre, destino_nombre, peso = dialogo.get_result()

            # Comprobar si ya existe un enlace entre los nodos
            if any(
                (arista.origen.nombre == origen_nombre and arista.destino.nombre == destino_nombre) or
                (arista.origen.nombre == destino_nombre and arista.destino.nombre == origen_nombre)
                for arista in self.aristas
            ):
                QMessageBox.information(self, "Error", "Ya existe un enlace entre estos nodos.")
                return

            origen = next(n for n in self.nodos if n.nombre == origen_nombre)
            destino = next(n for n in self.nodos if n.nombre == destino_nombre)

            arista = Arista(origen, destino, peso, self.escena)
            self.aristas.append(arista)
            origen.add_arista(arista)
            destino.add_arista(arista)


    def calcular_mst(self):
        """Calcular el MST con el algoritmo de Prim."""
        if not self.nodos or not self.aristas:
            QMessageBox.information(self, "Error", "No hay nodos o Enlaces en el grafo.")
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

        # Restablecer colores de aristas
        for arista in self.aristas:
            arista.linea.setPen(QPen(Qt.black, 2))

        # Marcar aristas del MST en rojo
        for arista in mst_aristas:
            arista.linea.setPen(QPen(Qt.red, 3))

        # Mostrar resultados en la tabla
        self.mostrar_resultados_mst(mst_aristas, total_costo)

    def mostrar_resultados_mst(self, mst_aristas, total_costo): 
        """Mostrar resultados del MST en la tabla."""
        # Crear un modelo de tabla estándar
        modelo = QStandardItemModel(len(mst_aristas), 3)
        
        # Configurar encabezados de columnas
        modelo.setHorizontalHeaderLabels(["Origen", "Destino", "Peso"])
        
        # Llenar el modelo
        for fila, arista in enumerate(mst_aristas):
            item_origen = QStandardItem(arista.origen.nombre)
            item_destino = QStandardItem(arista.destino.nombre)
            item_peso = QStandardItem(str(arista.peso))
            
            # Configurar las celdas como solo lectura
            item_origen.setFlags(item_origen.flags() & ~Qt.ItemIsEditable)
            item_destino.setFlags(item_destino.flags() & ~Qt.ItemIsEditable)
            item_peso.setFlags(item_peso.flags() & ~Qt.ItemIsEditable)
            
            # Agregar los elementos al modelo
            modelo.setItem(fila, 0, item_origen)
            modelo.setItem(fila, 1, item_destino)
            modelo.setItem(fila, 2, item_peso)
        
        # Asignar el modelo al TableView
        self.ui.tableview_mst.setModel(modelo)
        
        # Ajustar columnas al contenido
        self.ui.tableview_mst.resizeColumnsToContents()
        
        # Mostrar costo total
        self.ui.label_digitar_costo_total.setText(f" {total_costo}")



def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()