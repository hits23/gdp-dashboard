import streamlit as st


st.title('Hola')
st.write('¡Hola, actualización 3!')


import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import zipfile
import io

# URL del archivo ZIP en GitHub
url_zip = "https://github.com/hits23/gdp-dashboard/raw/main/Cred_Dep_Of.zip"

# Descargar el archivo ZIP y mantenerlo en memoria
response = requests.get(url_zip)
archivo_zip_en_memoria = io.BytesIO(response.content)

dataframes = []

# Leer el archivo ZIP desde la memoria
with zipfile.ZipFile(archivo_zip_en_memoria, 'r') as archivo_zip:
    nombres_archivos = archivo_zip.namelist()

    for nombre_archivo in nombres_archivos:
        with archivo_zip.open(nombre_archivo) as archivo:
            contenido = archivo.read().decode('utf-8')

            try:
                df = pd.read_csv(io.StringIO(contenido), delimiter=',', encoding='utf-8')
                df['nombre_archivo'] = nombre_archivo  # Agregar una columna con el nombre del archivo
                dataframes.append(df)
            except Exception as e:
                st.write(f'Error al leer {nombre_archivo}: {e}')

# Concatenar todos los DataFrames
df = pd.concat(dataframes, ignore_index=True)

# Título de la aplicación
st.title('Mi Primera Aplicación con Datos, Gráficas y Controles')

# Controles de selección de columna
col_chosen = st.radio('Selecciona una columna:', ['pop', 'lifeExp', 'gdpPercap'], index=1)

# Mostrar la tabla de datos
st.dataframe(df)

# Crear una gráfica interactiva
fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')

# Mostrar la gráfica
st.plotly_chart(fig)


