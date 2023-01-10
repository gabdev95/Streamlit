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

tamanho_grafico_barra = st.sidebar.slider('Tamanho do Gráfico de Barra', 200, 800, 400)

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

st.title('Spotify Tracks Dataset :musical_note:')
st.text('')

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

st.subheader('Dicionário')
st.caption('Para ter uma análise mais proveitosa, disponibilizou-se o dicionário abaixo, contendo informações sobre os dados que podem ser analisados neste dashboard.')
st.text(
    '''• Popularity = Popularidade;
    \n• Track genre = Gênero musical;
    \n• Tempo = Andamento geral estimado de uma faixa em batidas por minuto (BPM), ou seja, é a velocidade e ritmo de determinada peça (música) por minuto;
    \n• Danceability = Dançabilidade, diz o quanto uma música é dançavél, onde um valor de 0,0 é menos dançável e 1,0 é o mais dançável;
    \n• Energy = Energia, uma medida de 0,0 a 1,0 e representa uma medida perceptiva de intensidade e atividade;
    \n• Loudness = Sonoridade, o volume geral de uma faixa em decibéis (dB);
    \n• Explicit = Explícito, diz se uma faixa possui ou não letras explícitas;
    \n• Duration ms = Duração em milisegundos.'''
)
st.text('')

st.header('Gráficos gerais')
st.caption('Nos gráficos abaixo você é livre para escolher os dados de análise para os eixos x e y.')

st.subheader('Gráfico de Barra')
st.bar_chart(data=spotify, x=eixo_X_barra, y=eixo_Y_barra, height=tamanho_grafico_barra)

st.subheader('Gráfico de Linha')
st.line_chart(data=spotify, x=eixo_X_linha, y=eixo_Y_linha, height=tamanho_grafico_linha)

st.subheader('Gráfico de Quantidade')
grafico = px.treemap(spotify, path=[colunas])
st.write(grafico)

st.header(':red[Análises]')
st.caption('Os gêneros musicais estão em ordem alfabética: acoustic, alt-rock, ambient, black-metal, blues, breakbeat, cantopop, children, classical, comedy, dance, death-metal, detroit-techno, disney, dub, edm, eletronic, folk, fench, garage, gospel, grindcore, grunge, happy, hardcore, heavy-metal, honky-tonky, idm, indie, industrial, j-dance, j-pop, jazz, kids, latino, mandopop, metalcore, mpb, opera, árty, pop, power-pop, psych-pop, punk-rock, regge, rock, rockabilly, sad, samba, show-tunes, ska, songwriter, spanish, swedish, tango, trance e turkish.')

st.subheader('Popularidade x Gênero musical')
st.caption('Nesse gráfico é possível analisar a popularidade de cada gênero musical presente no dataset, quanto mais alto no eixo y (popularidade), mais popular é a música do eixo x que representa o genêro musical. Segundo o autor do dataset: "A popularidade de uma faixa é um valor entre 0 e 100, sendo 100 o mais popular. A popularidade é calculada por algoritmo e é baseada, em grande parte, no número total de reproduções que a faixa teve e quão recentes são essas reproduções." Por questões estruturias o gráfico abaixo no eixo y está com os valores: 0 e 60000, mas eles simbolizam respectivamente 0 e 60, porém é possível aumentar e diminuir o tamanho dos eixos com o "scroll" de seu mouse.')
st.caption('')
st.bar_chart(data=spotify, x="track_genre", y="popularity", height=600)

st.subheader('Dançabilidade X Gênero musical')
st.caption('Neste gráfico é possível analisar o quão dancavél é cada gênero musical. Por questões estruturias o gráfico abaixo no eixo y está com os valores: 0 e 800, mas eles simbolizam respectivamente 0.0 e 0.8, sabendo que "um valor de 0,0 é menos dançável e 1,0 é o mais dançável". Também é possível aumentar e diminuir o tamanho dos eixos com o "scroll" de seu mouse.')
st.bar_chart(data=spotify, x="track_genre", y="danceability", height=450)

st.subheader('Energia X Gênero musical')
st.caption('Neste gráfico é possível analisar a energia em cada gênero musical. Por questões estruturias o gráfico abaixo no eixo y está com os valores: 0 e 1000, mas eles simbolizam respectivamente 0.0 e 1.0, sabendo que "A energia é uma medida de 0,0 a 1,0 e representa uma medida perceptiva de intensidade e atividade". Também é possível aumentar e diminuir o tamanho dos eixos com o "scroll" de seu mouse.')
st.bar_chart(data=spotify, x="track_genre", y="energy", height=550)

# grafico = px.treemap(spotify, path=['popularity'])
# st.subheader('Popularidade')
# st.write(grafico)

# grafico = px.treemap(spotify, path=['popularity', 'track_genre'])
# # grafico.show()