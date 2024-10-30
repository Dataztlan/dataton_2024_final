### Análisis gráfico de las variaciones y relaciones del E-commerce con retail 

# Carga ggplot2
library(ggplot2)
library(reshape2)
library(scales)
library(readr)
library(dplyr)

# Lee el archivo CSV
datos <- read.csv("C:/Users/nexoc/Downloads/varicionescomercio.csv")

##  Variaciones de comercio digital

# Limpiar los datos eliminando columnas innecesarias y renombrando columnas inconsistentes
datos <- datos[, !names(datos) %in% c("Unnamed..6")]
names(datos)[names(datos) == "Variación._%_Comercio._al._por._menor"] <- "Variación_porcentual_Comercio_al_por_menor_no_digital"

# Eliminar los años 2023 y 2024
datos <- subset(datos, Año != 2023 & Año != 2024)

# Reestructura los datos en formato largo para ggplot2
datos_largos <- melt(datos, id.vars = "Año", 
                     variable.name = "Sector", 
                     value.name = "Variacion_Porcentual")

# Filtrar solo los sectores que quieres mostrar en la gráfica
sectores_interes <- c("Variación_porcentual_Total_digital", 
                      "Variación_porcentual_Comercio_al_por_mayor_digital",
                      "Variación_porcentual_Comercio_al_por_menor_digital",
                      "Variación_porcentual_Otros_servicios_digital")

datos_largos <- subset(datos_largos, Sector %in% sectores_interes)

# Crear la gráfica de columnas agrupadas con los sectores seleccionados
ggplot(datos_largos, aes(x = factor(Año), y = Variacion_Porcentual, fill = Sector)) +
  geom_col(position = "dodge", color = "black") +  # Color negro para los bordes
  scale_fill_manual(values = c("#D1C4E9", "#9575CD", "#673AB7", "#512DA8")) +  # Paleta morada
  geom_text(aes(label = round(Variacion_Porcentual, 1)), 
            position = position_dodge(width = 0.9), vjust = -0.3, size = 3) +  # Etiquetas de porcentaje
  labs(title = "Variación porcentual de Comercio Digital en México (2013-2022)",
       x = "Año",
       y = "Variación Porcentual (%)") +
  theme_minimal() +
  theme(legend.title = element_blank())

##Variación del comercio por menor

datos_minorista <- datos[, c("Año", "Variación porcentual Comercio al por menor")]

datos_minorista <- datos[, c("Año", "Variación_porcentual_Comercio_al_por_menor")]

# Renombra la columna para simplificar su uso
colnames(datos_minorista) <- c("Año", "Variacion_Porcentual")

# Crear la gráfica de columnas solo para "Comercio al por menor"
ggplot(datos_minorista, aes(x = factor(Año), y = Variacion_Porcentual)) +
  geom_col(fill = "#673AB7", color = "black") +  # Color morado con bordes negros
  geom_text(aes(label = round(Variacion_Porcentual, 1)), 
            vjust = -0.3, size = 3) +  # Etiquetas de porcentaje
  labs(title = "Variación porcentual de Comercio al por menor en México (2014-2022)",
       x = "Año",
       y = "Variación Porcentual (%)") +
  theme_minimal()

##Relación de consumo retail vs consumo digital

datos <- datos[, !names(datos) %in% c("Unnamed..6")]
names(datos) <- trimws(names(datos))  # Eliminar espacios adicionales en los nombres de las columnas

# Eliminar los años 2023 y 2024 si están presentes
datos <- subset(datos, Año != 2023 & Año != 2024)

# Selecciona solo las columnas necesarias
datos_minorista <- datos[, c("Año", "Variación_porcentual_Comercio_al_por_menor_digital", "Variacion_Porcentual_Comercio_Al_Por_Menor")]

# Reestructura los datos en formato largo para crear columnas agrupadas
datos_largos <- melt(datos_minorista, id.vars = "Año", 
                     variable.name = "Tipo_Comercio", 
                     value.name = "Variacion_Porcentual")

# Crear la gráfica de columnas agrupadas
ggplot(datos_largos, aes(x = factor(Año), y = Variacion_Porcentual, fill = Tipo_Comercio)) +
  geom_col(position = "dodge", color = "black") +  # Columnas agrupadas con bordes negros
  scale_fill_manual(values = c("#9575CD", "#673AB7")) +  # Colores morados para cada tipo
  geom_text(aes(label = round(Variacion_Porcentual, 1)), 
            position = position_dodge(width = 0.9), vjust = -0.3, size = 3) +  # Etiquetas de porcentaje
  labs(title = "Variación porcentual de Comercio al por menor en México (2012-2022)",
       x = "Año",
       y = "Variación Porcentual (%)") +
  theme_minimal() +
  theme(legend.title = element_blank())

data <- read_csv("C:/Users/nexoc/Downloads/Comercio digital en México.csv")

# Limpiar y transformar los datos
data$`Comercio al por mayor` <- as.numeric(gsub("[$,]", "", data$`Comercio al por mayor`))
data$`Comercio al por menor` <- as.numeric(gsub("[$,]", "", data$`Comercio al por menor`))
data$`Otros servicios` <- as.numeric(gsub("[$,]", "", data$`Otros servicios`))

# Convertir los datos en formato largo para ggplot2
library(tidyr)
data_long <- pivot_longer(data, cols = c(`Comercio al por mayor`, `Comercio al por menor`, `Otros servicios`),
                          names_to = "Tipo", values_to = "Valor")

# Convertir el año en factor para un mejor control del orden en el gráfico
data_long$Concepto <- factor(data_long$Concepto, levels = unique(data$Concepto))

# Crear el gráfico
ggplot(data_long, aes(x = Concepto, y = Valor, fill = Tipo)) +
  geom_bar(stat = "identity", position = "stack") +
  scale_y_continuous(labels = comma) +
  scale_fill_manual(values = c("#7D3C98", "#C39BD3", "#D2B4DE")) +
  labs(
    title = "¿Cómo ha evolucionado el e-commerce en México?",
    x = "Año",
    y = "Valores constantes base 2018 en millones de pesos",
    fill = "Tipo de Comercio"
  ) +
  theme_minimal() +
  annotate("text", x = c(1, 2, 3), y = -50000, label = "*", color = "black", size = 5, hjust = -0.1) +
  annotate("text", x = c(14, 15), y = -50000, label = "*", color = "black", size = 5, hjust = -0.1) +
  theme(plot.title = element_text(hjust = 0.5)) +
  labs(caption = "Elaboración propia con datos del INEGI VABCOEL.\n*Años 2010, 2011 y 2012 son extrapolaciones propias. Años 2023 y 2024 son proyecciones propias.") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

##Gráfica E-commerce como porcentaje del PIB EUA vs México

datos <- read.csv("C:/Users/nexoc/Downloads/US_Mexico_Ecommerce_Percentage_of_GDP.csv", encoding = "latin1")
colnames(datos)
datos <- datos %>%
  mutate(Tipo_Mexico = ifelse(as.numeric(Año) < 2012, "Extrapolación", 
                              ifelse(as.numeric(Año) %in% c(2024, 2025, 2026), "Proyección", "Datos reales")),
         Tipo_EUA = ifelse(as.numeric(Año) %in% c(2024, 2025, 2026), "Proyección", "Datos reales"))

# Transformar los datos a formato largo para ggplot2
datos_largo <- datos %>%
  pivot_longer(cols = c("E.commerce.México.como.proporción.del.PIB", 
                        "E.commerce.EUA.como.proporción.del.PIB"), 
               names_to = "País", 
               values_to = "Ecommerce_GDP_Percentage") %>%
  mutate(País = ifelse(País == "E.commerce.México.como.proporción.del.PIB", "México", "EUA"),
         Tipo = ifelse(País == "México", Tipo_Mexico, Tipo_EUA))

# Definir la paleta de colores: rosa para EUA y morado para México
colores_personalizados <- c("México - Extrapolación" = "#BDA0CB", 
                            "México - Datos reales" = "#6A0DAD", 
                            "México - Proyección" = "#D8BFD8",
                            "EUA - Datos reales" = "#FF69B4", 
                            "EUA - Proyección" = "#FFB6C1")

# Crear una columna combinada para país y tipo para asignar colores específicos
datos_largo <- datos_largo %>%
  mutate(País_Tipo = paste(País, "-", Tipo))

# Crear el gráfico con ajustes de etiquetas y ejes
ggplot(datos_largo, aes(x = as.numeric(Año), y = Ecommerce_GDP_Percentage, color = País_Tipo, group = País_Tipo)) +
  geom_line(aes(linetype = Tipo), size = 1.2) +
  geom_point(aes(shape = Tipo), size = 3) +
  scale_color_manual(values = colores_personalizados) +
  labs(title = "Comparativa de México vs E.U.A de la aportación de e-commerce como porcentaje del PIB",
       x = "Año",
       y = "Porcentaje del PIB",
       caption = "*Los datos de México antes de 2012 son extrapolaciones; 2024, 2025 y 2026 son proyecciones.\nElaboración propia con datos del INEGI VABCOEL y St. Louis FED") +
  scale_x_continuous(breaks = seq(min(as.numeric(datos$Año)), max(as.numeric(datos$Año)), by = 1)) +  # Mostrar todos los años
  scale_y_continuous(breaks = seq(0, max(datos_largo$Ecommerce_GDP_Percentage, na.rm = TRUE), by = 0.5)) + # Ajustar los incrementos del eje Y
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, face = "bold", size = 16),
        axis.title = element_text(size = 14),
        axis.text = element_text(size = 12),
        legend.position = "bottom",
        plot.caption = element_text(hjust = 0, size = 10))
