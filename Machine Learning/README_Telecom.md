# 📊 Análisis de Consumo de Planes Telefónicos - Sprint 9

Este proyecto analiza el **comportamiento de los usuarios** de una compañía telefónica y compara el consumo de dos planes principales:  
- **Smart (Surf)**  
- **Ultra**  

El análisis se centra en identificar patrones de uso y determinar cuál de los planes genera mayores ingresos, apoyando la toma de decisiones estratégicas de la empresa.

---

## 🎯 Objetivo
- Comprender cómo los usuarios consumen servicios bajo los planes Smart y Ultra.  
- Evaluar ingresos generados por cada plan.  
- Identificar diferencias significativas en consumo de minutos, mensajes y datos móviles.  
- Recomendar estrategias para optimizar precios y marketing.

---

## 📂 Dataset
**Archivo utilizado:** `users_behavior.csv`  

Incluye información como:  
- Número de llamadas.  
- Minutos consumidos.  
- Mensajes enviados.  
- Datos de internet (MB usados).  
- Plan contratado (Smart o Ultra).  
- Ingresos generados.

---

## 🛠️ Herramientas y Tecnologías
- **Lenguaje:** Python 3.x  
- **Entorno:** Jupyter Notebook (`Srpint 9.ipynb`)  
- **Librerías principales:**
  - `pandas` → manipulación y limpieza de datos  
  - `numpy` → operaciones numéricas  
  - `matplotlib` y `seaborn` → visualización de datos  
  - `scipy` → pruebas de hipótesis y análisis estadístico  

---

## 📊 Metodología
1. **Carga y exploración de datos** → revisión de la calidad de la información.  
2. **Preprocesamiento** → manejo de valores nulos y conversión de tipos de datos.  
3. **EDA (Exploratory Data Analysis)** → análisis de consumo por usuarios y planes.  
4. **Comparación de ingresos** → entre los planes Smart y Ultra.  
5. **Pruebas de hipótesis** → para determinar si existen diferencias estadísticamente significativas en el consumo y los ingresos.  

---

## 📈 Resultados esperados
- Los usuarios del plan **Smart** suelen sobrepasar los límites contratados, generando ingresos adicionales por cargos extra.  
- Los usuarios del plan **Ultra**, aunque pagan más por el servicio, tienden a no exceder sus límites.  
- En términos de ingreso promedio por usuario:  
  - Smart ≈ 63 USD  
  - Ultra ≈ 70 USD  
- Se concluye que ambos planes son rentables, pero el **plan Ultra asegura ingresos más estables** mientras que el plan Smart depende del sobreuso.  

---

## 🚀 Ejecución del proyecto

1. Clonar el repositorio:  
```bash
git clone https://github.com/jfrf98/portafolio.git
cd portafolio
```

2. Abrir el notebook:  
```bash
jupyter notebook "Srpint 9.ipynb"
```

3. Ejecutar las celdas paso a paso para reproducir el análisis.

---

## 📌 Próximos pasos
- Implementar modelos de **machine learning** para predecir el consumo de nuevos clientes.  
- Realizar segmentación de clientes mediante **clustering**.  
- Simular escenarios de ajuste de precios para optimizar ingresos.  

---
