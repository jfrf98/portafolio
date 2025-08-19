# StreamlitDeploy - Vehicles Analysis

Este proyecto es una aplicación interactiva desarrollada en **Streamlit** para el análisis de datos de vehículos en EE. UU.  
Utiliza un dataset (`vehicles_us.csv` / `vehicles_us.xlsx`) que contiene información de anuncios de autos, incluyendo características como precio, modelo, año, odómetro, condición, entre otros.

---

## 🎯 Objetivo
- Explorar y analizar datos de vehículos.  
- Identificar patrones y relaciones entre características (ej. año vs precio, odómetro vs condición).  
- Visualizar información de forma clara e interactiva para facilitar la interpretación.

---

## 🛠️ Herramientas y Tecnologías
- **Lenguaje:** Python 3.x  
- **Framework Web:** [Streamlit](https://streamlit.io/)  
- **Librerías principales:**
  - `pandas` → carga y manipulación de datos
  - `numpy` → cálculos numéricos
  - `matplotlib` / `plotly` → visualizaciones
  - `openpyxl` → lectura de archivos Excel
- **Datos:** `vehicles_us.csv` o `vehicles_us.xlsx`  

---

## 📂 Estructura del proyecto
```
StreamlitDeploy/
│── app.py                # Script principal de la aplicación Streamlit
│── vehicles_us.csv       # Dataset en formato CSV
│── vehicles_us.xlsx      # Dataset en formato Excel
│── requirements.txt      # Dependencias necesarias
└── README.md             # Este archivo
```

---

## 🚀 Cómo ejecutar la aplicación

### 1. Clonar el repositorio
```bash
git clone https://github.com/jfrf98/portafolio.git
cd portafolio/StreamlitDeploy
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar Streamlit
```bash
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador en `http://localhost:8501`.

---

## ✨ Funcionalidades
- Visualización de estadísticas descriptivas del dataset.  
- Gráficos interactivos para explorar:
  - Distribución de precios de vehículos.  
  - Relación entre año del vehículo y precio.  
  - Relación entre odómetro y condición.  
- Opciones de filtrado dinámico para personalizar la exploración.  

---

## 📌 Próximos pasos
- Incluir modelos predictivos simples (ej. regresión lineal para estimar precios).  
- Permitir al usuario subir sus propios datasets para analizar.  
- Desplegar la app en **Streamlit Cloud** para acceso en línea.  

---
