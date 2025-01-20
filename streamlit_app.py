import streamlit as st
import pandas as pd
import plotly.express as px

# Incorporar datos
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Título de la aplicación
st.title('Mi Primera Aplicación con Datos, Gráficos y Controles')

# División en radio botones
col_chosen = st.radio('Elige una columna para visualizar', options=['pop', 'lifeExp', 'gdpPercap'], index=1)

# Mostrar datos en una tabla
st.dataframe(df.head(6))

# Actualización del gráfico en función de la columna elegida
fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
st.plotly_chart(fig)
