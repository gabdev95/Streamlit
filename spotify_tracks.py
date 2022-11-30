import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Spotify Tracks Dataset')

@st.cache
def carregar_dados(caminho):
    data = pd.read_csv(caminho)
    return data

spotify = carregar_dados('data/dataset.csv')

if st.checkbox('Mostrar dataset'):
    st.subheader('Dataset padrão')
    st.dataframe(spotify)

@st.cache
def analise():   
    medias = spotify.mean()
    vazio = spotify.isnull()
    soma_vazio = spotify.isnull().sum()
    return medias, vazio, soma_vazio

medias, vazio, soma_vazio = analise()

st.subheader('Médias de cada coluna')
st.table(medias)

st.subheader('Valores vazios')
st.dataframe(vazio)

st.subheader('Soma dos valores vazios em cada coluna')
st.dataframe(soma_vazio)

st.subheader('Popularidade X Duration em ms')
st.bar_chart(data=spotify, x='popularity', y='duration_ms')
st.subheader('Popularidade X Dançabilidade')
st.bar_chart(data=spotify, x='popularity', y='danceability')
st.subheader('Energia X Popularidade')
st.line_chart(data=spotify, x='energy', y='popularity')
st.subheader('Gênero X Popularidade')
st.bar_chart(data=spotify, x='track_genre', y='popularity')

grafico = px.treemap(spotify, path=['track_genre'])
st.subheader('Gêneros')
st.write(grafico)

grafico = px.treemap(spotify, path=['popularity'])
st.subheader('Popularidade')
st.write(grafico)

grafico = px.treemap(spotify, path=['popularity', 'track_genre'])
# grafico.show()