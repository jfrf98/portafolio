import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")


st.header("Car Data")

build_histogram = st.checkbox("Construir Histograma")

columna = st.selectbox("Seleccionar columna para histograma", car_data.columns)

if build_histogram: # al hacer click en el boton...

    # escribir mensaje
    st.write("Creacion de un histograma para el conjunto de datos de anuncios de ventas de coches")

    # crea el histograma
    fig = px.histogram(car_data, x=columna)

    # muestra el histograma interctivo - grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox("Construir Grafico de Dispersion")

eje_x = st.selectbox("Seleccionar el eje x", car_data.columns)
eje_y = st.selectbox("Seleccionar el eje y", car_data.columns)

if build_scatter: # al hacer click el boton...
    
    # escribir mensaje
    st.write("Creacion de grafico de dispersion para el conjunto de datos de anuncios de ventas de coches")
    
    # crear grafico de dispersion
    fig = px.scatter(car_data, x=eje_x, y=eje_y)

    # muestra el grafico de dispersion interctivo - grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



