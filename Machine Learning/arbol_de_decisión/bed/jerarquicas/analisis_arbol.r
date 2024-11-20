if (!require("jsonlite")) install.packages("jsonlite", dependencies=TRUE)  
if (!require("ggplot2")) install.packages("ggplot2", dependencies=TRUE)  
library(jsonlite) 
library(ggplot2)   


extraer_informacion <- function(nodo) {
  # Crear un data frame vacío para almacenar los resultados
  resultados <- data.frame(
    edad = character(),       
    ocupacion = character(),   
    stringsAsFactors = FALSE   
  )
  
  # Función interna para procesar cada nodo recursivamente
  procesar_nodo <- function(nodo, edad_actual = NULL) {
    # Verificar si el nodo es una lista válida
    if (is.list(nodo)) {
      # Si el nodo representa edad, actualizar la edad actual
      if (!is.null(nodo$criterio) && nodo$criterio == "edad") {
        edad_actual <- nodo$valor
      }
      
      # Si el nodo representa ocupación, crear nuevo registro
      if (!is.null(nodo$criterio) && nodo$criterio == "ocupacion") {
        nuevo_registro <- data.frame(
          edad = edad_actual,
          ocupacion = nodo$valor,
          stringsAsFactors = FALSE
        )
        resultados <<- rbind(resultados, nuevo_registro)  # Agregar al data frame global
      }
      
      # Procesar recursivamente los nodos hijos
      if (!is.null(nodo$hijos)) {
        for (hijo in nodo$hijos) {
          procesar_nodo(hijo, edad_actual)
        }
      }
    }
  }
  
  # Iniciar el procesamiento desde el nodo raíz
  procesar_nodo(nodo)
  return(resultados)
}


tryCatch({
  datos_arbol <- fromJSON("C:/Programacion Universidad/Semestre 4/Machine Learning/arbol_de_decisión/bed/jerarquicas/arbol_decision.json", 
                          simplifyVector = FALSE)
  
  cat("Estructura del árbol:\n")
  str(datos_arbol)
  
  informacion_arbol <- extraer_informacion(datos_arbol)
  
  cat("\nDatos extraídos del árbol:\n")
  print(informacion_arbol)
  
  if (nrow(informacion_arbol) > 0) {
    # 1. Grafico de barras
    p1 <- ggplot(informacion_arbol, aes(x = edad, fill = ocupacion)) +
      geom_bar(position = "dodge") +
      scale_fill_manual(values = c(
        "Estudiante" = "#FF4B4B",    
        "Trabajador" = "#4B7BFF",    
        "Jubilado" = "#FFD700"       
      )) +
      labs(
        title = "Distribución por Edad y Ocupación",
        subtitle = "Análisis de grupos por rango etario",
        x = "Rango de Edad",
        y = "Cantidad",
        fill = "Ocupación"
      ) +
      theme_minimal() +
      theme(
        plot.title = element_text(hjust = 0.5, size = 16, face = "bold", color = "#2E2E2E"),
        plot.subtitle = element_text(hjust = 0.5, size = 12, color = "#4A4A4A"),
        axis.text.x = element_text(angle = 45, hjust = 1, color = "#2E2E2E"),
        axis.title = element_text(color = "#2E2E2E", face = "bold"),
        legend.position = "top",
        panel.grid.major = element_line(color = "#E0E0E0"),
        panel.grid.minor = element_line(color = "#F0F0F0")
      )
    
    # 2. Grafico de burbujas
    p2 <- ggplot(informacion_arbol) +
      geom_count(aes(x = edad, y = ocupacion, color = ocupacion, size = ..n..), alpha = 0.8) +
      scale_size_area(max_size = 20) +
      scale_color_manual(values = c(
        "Estudiante" = "#FF4B4B",   
        "Trabajador" = "#4B7BFF",    
        "Jubilado" = "#FFD700"       
      )) +
      labs(
        title = "Mapa de Distribución",
        subtitle = "Tamaño del punto indica la frecuencia",
        x = "Rango de Edad",
        y = "Ocupación",
        size = "Frecuencia",
        color = "Ocupación"
      ) +
      theme_minimal() +
      theme(
        plot.title = element_text(hjust = 0.5, size = 16, face = "bold", color = "#2E2E2E"),
        plot.subtitle = element_text(hjust = 0.5, size = 12, color = "#4A4A4A"),
        axis.text.x = element_text(angle = 45, hjust = 1, color = "#2E2E2E"),
        axis.title = element_text(color = "#2E2E2E", face = "bold"),
        legend.position = "top",
        panel.grid.major = element_line(color = "#E0E0E0"),
        panel.grid.minor = element_line(color = "#F0F0F0")
      )
    
    print(p1)
    print(p2)
    
    cat("\nResumen de datos:\n")
    print(table(informacion_arbol$edad, informacion_arbol$ocupacion))
    
  } else {
    cat("No se encontraron datos para visualizar.\n")
  }
}, error = function(e) {
  cat("Error al procesar los datos:", conditionMessage(e), "\n")
  print(str(datos_arbol))
})