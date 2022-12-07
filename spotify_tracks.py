import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.sidebar.header('Dashboard')

st.sidebar.subheader('Gráficos de Barras:')
eixo_X_barra = st.sidebar.selectbox('Eixo x do gráfico de barra', (
    'popularity',
    'track_genre',
    'tempo',
    'danceability',
    'energy',
    'loudness',
    'explicit',
    'duration_ms'
))

eixo_Y_barra = st.sidebar.selectbox(('Eixo y do gráfico de barra'),(
    'popularity',
    'track_genre',
    'tempo',
    'danceability',
    'energy',
    'loudness',
    'explicit',
    'duration_ms'
))

st.sidebar.subheader('Gráficos de Linhas: ')
eixo_X_linha = st.sidebar.selectbox('Eixo x do gráfico de linha', (
    'popularity',
    'track_genre',
    'tempo',
    'danceability',
    'energy',
    'loudness',
    'explicit',
    'duration_ms'
))

tamanho_grafico_barra = st.sidebar.slider('Tamanho do Gráfico de Barra', 200, 800, 400)


eixo_Y_linha = st.sidebar.selectbox(('Eixo y do gráfico de linha'),(
    'popularity',
    'track_genre',
    'tempo',
    'danceability',
    'energy',
    'loudness',
    'explicit',
    'duration_ms'
))

tamanho_grafico_linha = st.sidebar.slider('Tamanho do Gráfico de Linha', 200, 800, 250)

st.sidebar.subheader('Gráficos de Quantidade:')
colunas = st.sidebar.selectbox('Opções', (
    'popularity',
    'duration_ms',
    'explicit',
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acoustiness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'track_genre',
))

st.title('Spotify Tracks Dataset')

@st.cache
def carregar_dados(caminho):
    data = pd.read_csv(caminho)
    return data

spotify = carregar_dados('data/dataset.csv')

if st.checkbox('Mostrar dataset completo'):
    st.subheader('Dataset Completo')
    st.dataframe(spotify)

@st.cache
def analise(dataset):   
    medias = dataset.mean()
    vazio = dataset.isnull()
    soma_vazio = dataset.isnull().sum()
    return medias, vazio, soma_vazio

medias, vazio, soma_vazio = analise(spotify)

if st.checkbox('Mostrar análises preliminares do dataset'):
    st.subheader('Médias de cada coluna')
    st.table(medias)

    # st.subheader('Valores vazios')
    # st.dataframe(vazio)

    st.subheader('Soma dos valores vazios em cada coluna')
    st.table(soma_vazio)

st.subheader('Gráfico de Barra')
st.bar_chart(data=spotify, x=eixo_X_barra, y=eixo_Y_barra, height=tamanho_grafico_barra)

st.subheader('Gráfico de Linha')
st.line_chart(data=spotify, x=eixo_X_linha, y=eixo_Y_linha, height=tamanho_grafico_linha)

st.subheader('Gráfico de Quantidade')
grafico = px.treemap(spotify, path=[colunas])
st.write(grafico)

# grafico = px.treemap(spotify, path=['popularity'])
# st.subheader('Popularidade')
# st.write(grafico)

# grafico = px.treemap(spotify, path=['popularity', 'track_genre'])
# # grafico.show()