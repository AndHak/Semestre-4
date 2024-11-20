import sys
import os
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QLineEdit, QPushButton, QLabel, QTextEdit)
from PySide6.QtCore import Qt

ruta_actual = os.path.dirname(__file__)

class DecisionArbolAnalyzer:
    def __init__(self, json_data):
        self.Arbol = json_data
        self.ocupacion_por_edad = self._analizar_ocupaciones_por_edad()
    
    def _analizar_ocupaciones_por_edad(self):
        """Analiza el árbol y cuenta todas las ocupaciones por rango de edad"""
        ocupacion_por_edad = {}
        
        def recorrer_arbol(nodo):
            if nodo['criterio'] == 'edad':
                edad = nodo['valor']
                ocupacion_por_edad[edad] = {'Estudiante': 0, 'Trabajador': 0, 'Jubilado': 0}
                
                for hijo in nodo['hijos']:
                    if hijo['criterio'] == 'ocupacion':
                        ocupacion = hijo['valor']
                        ocupacion_por_edad[edad][ocupacion] += 1
            
            # Recorrer hijos recursivamente
            for hijo in nodo['hijos']:
                recorrer_arbol(hijo)
        
        recorrer_arbol(self.Arbol)
        return ocupacion_por_edad
    
    def obtener_info_ocupacion(self, ocupacion):
        """Retorna información sobre una ocupación específica"""
        rangos_con_ocupacion = []
        for edad, datos in self.ocupacion_por_edad.items():
            if datos[ocupacion] > 0:
                rangos_con_ocupacion.append(edad)
        return rangos_con_ocupacion
    
    def obtener_estadisticas_completas(self):
        """Retorna estadísticas completas de todas las ocupaciones"""
        estadisticas = {
            'Estudiante': [],
            'Trabajador': [],
            'Jubilado': []
        }
        for edad, datos in self.ocupacion_por_edad.items():
            for ocupacion, cantidad in datos.items():
                if cantidad > 0:
                    estadisticas[ocupacion].append(edad)
        return estadisticas

class MainWindow(QMainWindow):
    def __init__(self, analyzer):
        super().__init__()
        self.analyzer = analyzer
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("IA Basica")
        self.setMinimumWidth(600)
        
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        titulo = QLabel("IA Basica")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin: 15px; color: #2C3E50;")
        layout.addWidget(titulo)
        
        label = QLabel("Puedes preguntarme sobre estudiantes, trabajadores o jubilados y sus rangos de edad")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #7F8C8D; margin-bottom: 10px;")
        layout.addWidget(label)
        
        self.question_input = QLineEdit()
        self.question_input.setPlaceholderText("Ejemplo: ¿En qué edades hay más estudiantes?")
        self.question_input.setStyleSheet("padding: 8px; border-radius: 4px; border: 1px solid #BDC3C7;")
        layout.addWidget(self.question_input)
        
        analizar_button = QPushButton("Preguntar")
        analizar_button.setStyleSheet("""
            QPushButton {
                background-color: #3498DB;
                color: white;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
        """)
        analizar_button.clicked.connect(self.analyze_question)
        layout.addWidget(analizar_button)
        
        self.salida_info = QTextEdit()
        self.salida_info.setReadOnly(True)
        self.salida_info.setMinimumHeight(150)
        self.salida_info.setStyleSheet("""
            QTextEdit {
                background-color: #F8F9FA;
                border-radius: 4px;
                padding: 10px;
                border: 1px solid #BDC3C7;
            }
        """)
        layout.addWidget(self.salida_info)
        
        # Botón para mostrar estadísticas completas
        boton_datos = QPushButton("Mostrar todas las estadísticas")
        boton_datos.setStyleSheet("""
            QPushButton {
                background-color: #2ECC71;
                color: white;
                padding: 8px;
                border-radius: 4px;
                border: none;
            }
            QPushButton:hover {
                background-color: #27AE60;
            }
        """)
        boton_datos.clicked.connect(self.show_all_data)
        layout.addWidget(boton_datos)
    
    def analyze_question(self):
        question = self.question_input.text().lower()
        
        # Palabras clave para cada tipo de ocupación
        keywords = {
            'estudiante': ['estudiante', 'estudian', 'estudiantes', 'estudiar'],
            'trabajador': ['trabajo', 'trabajan', 'trabajador', 'trabajadores', 'trabajando'],
            'jubilado': ['jubilado', 'jubilados', 'jubilacion', 'pensionado', 'retirado']
        }
        
        # Determinar qué ocupación se está preguntando
        ocupacion_preguntada = None
        for ocupacion, palabras in keywords.items():
            if any(palabra in question for palabra in palabras):
                ocupacion_preguntada = ocupacion.capitalize()
                break
        
        if ocupacion_preguntada:
            rangos = self.analyzer.obtener_info_ocupacion(ocupacion_preguntada)
            if rangos:
                if len(rangos) == 1:
                    response = f"Los {ocupacion_preguntada.lower()}s se encuentran en el rango de {rangos[0]}."
                else:
                    response = f"Los {ocupacion_preguntada.lower()}s se encuentran en los siguientes rangos de edad: {', '.join(rangos)}."
                
                # Agregar información adicional
                if ocupacion_preguntada == "Estudiante":
                    response += "\nEsto es típico ya que la mayoría de los estudiantes son jóvenes adultos."
                elif ocupacion_preguntada == "Trabajador":
                    response += "\nComo puedes ver, la mayor concentración de trabajadores está en la edad productiva."
                elif ocupacion_preguntada == "Jubilado":
                    response += "\nNaturalmente, los jubilados se encuentran en los rangos de edad más avanzada."
            else:
                response = f"No encontré información sobre {ocupacion_preguntada.lower()}s en los datos."
        else:
            response = "Por favor, hazme una pregunta sobre estudiantes, trabajadores o jubilados y sus rangos de edad."
        
        self.salida_info.setText(response)
    
    def show_all_data(self):
        stats = self.analyzer.obtener_estadisticas_completas()
        text = "Análisis completo de ocupaciones por edad:\n\n"
        
        for ocupacion, rangos in stats.items():
            if rangos:
                text += f"   {ocupacion}s:\n"
                text += f"   Se encuentran en: {', '.join(rangos)}\n\n"
        
        self.salida_info.setText(text)

def main():
    try:
        with open(os.path.join(ruta_actual, 'bed/jerarquicas/arbol_decision.json'), 'r', encoding='utf-8') as file:
            Arbol_data = json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró el archivo JSON")
        return
    
    app = QApplication(sys.argv)
    analyzer = DecisionArbolAnalyzer(Arbol_data)
    window = MainWindow(analyzer)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()