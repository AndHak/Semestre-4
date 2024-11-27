# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainApp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_grafo = QWidget(self.centralwidget)
        self.widget_grafo.setObjectName(u"widget_grafo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_grafo.sizePolicy().hasHeightForWidth())
        self.widget_grafo.setSizePolicy(sizePolicy)
        self.widget_grafo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.widget_grafo)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_3.addWidget(self.widget_grafo, 1, 0, 1, 1)

        self.menu_widget = QWidget(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setStyleSheet(u"QPushButton {  \n"
"    border: none;  \n"
"    border-radius: 5px;  \n"
"    background-color: transparent; \n"
"}  \n"
"\n"
"QPushButton:hover {  \n"
"    background-color: rgb(236, 236, 236);  \n"
"}  \n"
"\n"
"QPushButton:pressed {  \n"
"    background-color: rgb(253, 253, 253);  \n"
"} ")
        self.horizontalLayout_2 = QHBoxLayout(self.menu_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.add_nodo_button = QPushButton(self.menu_widget)
        self.add_nodo_button.setObjectName(u"add_nodo_button")
        self.add_nodo_button.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(12)
        self.add_nodo_button.setFont(font)
        self.add_nodo_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/icons/add_node.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_nodo_button.setIcon(icon)
        self.add_nodo_button.setIconSize(QSize(40, 40))
        self.add_nodo_button.setCheckable(True)
        self.add_nodo_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.add_nodo_button)

        self.delete_nodo_button = QPushButton(self.menu_widget)
        self.delete_nodo_button.setObjectName(u"delete_nodo_button")
        self.delete_nodo_button.setMinimumSize(QSize(0, 50))
        self.delete_nodo_button.setFont(font)
        self.delete_nodo_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/icons8-delete-node-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_nodo_button.setIcon(icon1)
        self.delete_nodo_button.setIconSize(QSize(40, 40))
        self.delete_nodo_button.setCheckable(True)
        self.delete_nodo_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.delete_nodo_button)

        self.hacer_enlace_button = QPushButton(self.menu_widget)
        self.hacer_enlace_button.setObjectName(u"hacer_enlace_button")
        self.hacer_enlace_button.setMinimumSize(QSize(0, 50))
        self.hacer_enlace_button.setFont(font)
        self.hacer_enlace_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/icons8-link-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hacer_enlace_button.setIcon(icon2)
        self.hacer_enlace_button.setIconSize(QSize(40, 40))
        self.hacer_enlace_button.setCheckable(True)
        self.hacer_enlace_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.hacer_enlace_button)

        self.delete_link = QPushButton(self.menu_widget)
        self.delete_link.setObjectName(u"delete_link")
        self.delete_link.setMinimumSize(QSize(0, 50))
        self.delete_link.setFont(font)
        self.delete_link.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/icons8-link-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_link.setIcon(icon3)
        self.delete_link.setIconSize(QSize(40, 40))
        self.delete_link.setCheckable(True)
        self.delete_link.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.delete_link)

        self.delete_all_button = QPushButton(self.menu_widget)
        self.delete_all_button.setObjectName(u"delete_all_button")
        self.delete_all_button.setMinimumSize(QSize(0, 50))
        self.delete_all_button.setFont(font)
        self.delete_all_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/icons8-delete-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_all_button.setIcon(icon4)
        self.delete_all_button.setIconSize(QSize(40, 40))
        self.delete_all_button.setCheckable(True)
        self.delete_all_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.delete_all_button)

        self.calcular_mst_button = QPushButton(self.menu_widget)
        self.calcular_mst_button.setObjectName(u"calcular_mst_button")
        self.calcular_mst_button.setMinimumSize(QSize(0, 50))
        self.calcular_mst_button.setFont(font)
        self.calcular_mst_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/icons8-play-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calcular_mst_button.setIcon(icon5)
        self.calcular_mst_button.setIconSize(QSize(40, 40))
        self.calcular_mst_button.setCheckable(True)
        self.calcular_mst_button.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.calcular_mst_button)


        self.gridLayout_3.addWidget(self.menu_widget, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(123, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/Icons/icons/icons8-algorithm-100.png"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(19)
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.label_desarrollado_por = QLabel(self.centralwidget)
        self.label_desarrollado_por.setObjectName(u"label_desarrollado_por")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_desarrollado_por.setFont(font2)
        self.label_desarrollado_por.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_desarrollado_por, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.dock_mov = QWidget(self.centralwidget)
        self.dock_mov.setObjectName(u"dock_mov")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dock_mov.sizePolicy().hasHeightForWidth())
        self.dock_mov.setSizePolicy(sizePolicy1)
        self.dock_mov.setStyleSheet(u"background-color: rgb(226, 237, 245);")
        self.gridLayout = QGridLayout(self.dock_mov)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.mst_label = QLabel(self.dock_mov)
        self.mst_label.setObjectName(u"mst_label")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.mst_label.setFont(font3)

        self.gridLayout.addWidget(self.mst_label, 1, 0, 1, 1)

        self.tableview_mst = QTableView(self.dock_mov)
        self.tableview_mst.setObjectName(u"tableview_mst")
        self.tableview_mst.setStyleSheet(u"QTableView {  \n"
"    border: 1px solid gray;  \n"
"    gridline-color: lightgray; /* Color de las l\u00edneas de la cuadr\u00edcula */  \n"
"    background-color: white;  \n"
"    selection-background-color: lightblue; /* Color de selecci\u00f3n */  \n"
"    selection-color: black; /* Color del texto seleccionado */  \n"
"}  \n"
"\n"
"QHeaderView::section {  \n"
"    background-color: #e0e0e0; /* Color de cabecera */  \n"
"    padding: 5px;  \n"
"    border: 1px solid gray;  \n"
"}  ")

        self.gridLayout.addWidget(self.tableview_mst, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.costo_total_label = QLabel(self.dock_mov)
        self.costo_total_label.setObjectName(u"costo_total_label")
        self.costo_total_label.setFont(font3)

        self.horizontalLayout.addWidget(self.costo_total_label)

        self.label_digitar_costo_total = QLabel(self.dock_mov)
        self.label_digitar_costo_total.setObjectName(u"label_digitar_costo_total")
        font4 = QFont()
        font4.setPointSize(15)
        self.label_digitar_costo_total.setFont(font4)

        self.horizontalLayout.addWidget(self.label_digitar_costo_total)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 98, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 99, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.dock_mov, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_nodo_button.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Nodo", None))
        self.delete_nodo_button.setText(QCoreApplication.translate("MainWindow", u"Borrar nodo", None))
        self.hacer_enlace_button.setText(QCoreApplication.translate("MainWindow", u"Hacer Enlace", None))
        self.delete_link.setText(QCoreApplication.translate("MainWindow", u"Borrar enlace", None))
        self.delete_all_button.setText(QCoreApplication.translate("MainWindow", u"Eliminar todo", None))
        self.calcular_mst_button.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Algoritmo de Prim", None))
        self.label_desarrollado_por.setText(QCoreApplication.translate("MainWindow", u"Andres Felipe Martinez Guerra | Sebastian David Ordo\u00f1ez Bola\u00f1os", None))
        self.mst_label.setText(QCoreApplication.translate("MainWindow", u"M.S.T", None))
        self.costo_total_label.setText(QCoreApplication.translate("MainWindow", u"Costo Total:", None))
        self.label_digitar_costo_total.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

