import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import random


st.set_page_config(
    page_title='Analises', 
    page_icon='assets\logo.png', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

st.title('Analise Preliminares')
st.caption('Nos gráficos abaixo você é livre para escolher os dados de análise para os eixos de x, y ou ambos.')

nd = pd.read_parquet('dataset_sem_inconsistencias.parquet')

# Esse comando deixa o carregamento muito lento
# media = nd.mean(numeric_only=True)

st.sidebar.title('Barra lateral')
st.sidebar.subheader('Gráfico de Barra Horizontal 1: ')

eixo_x_barra_horizontal_1 = st.sidebar.selectbox(
    'Eixo X - gráfico de barra horizontal 1', (
        'popularidade',
        'duracao(min)',
        'explicita' ,
        'dancabilidade',
        'energia',
        'altura(db)',
        'falada',
        'acustica',
        'instrumental',
        'ao vivo',
        'valencia',
        'bpm',
        'compasso',
    ))


# st.sidebar.subheader('Gráfico de Barra Horizontal 2: ')
# eixo_y_barra_horizontal_2 = st.sidebar.selectbox(
#     'Eixo Y - gráfico de barra horizontal 2', (
#         'artistas',
#         'album',
#        'nome',
#        'genero',
#     ))

# eixo_x_barra_horizontal_2 = st.sidebar.selectbox(
#     'Eixo X - gráfico de barra horizontal 2', (
#         'popularidade',
#         'duracao(min)',
#         'explicita' ,
#         'dancabilidade',
#         'energia',
#         'altura(db)',
#         'falada',
#         'acustica',
#         'instrumental',
#         'ao vivo',
#         'valencia',
#         'bpm',
#         'compasso',
#     ))


st.sidebar.subheader('Gráfico de Barra Horizontal 2: ')

eixo_x_barra_horizontal_3 = st.sidebar.selectbox(
    'Eixo X - gráfico de barra horizontal 2', (
        'popularidade',
        'duracao(min)',
        'explicita' ,
        'dancabilidade',
        'energia',
        'altura(db)',
        'falada',
        'acustica',
        'instrumental',
        'ao vivo',
        'valencia',
        'bpm',
        'compasso',
    ))

eixo_y_barra_horizontal_3 = st.sidebar.selectbox(
    'Eixo Y - gráfico de barra horizontal 2', (
        'acoustic', 'alt-rock', 'ambient', 
        'black-metal', 'blues', 'breakbeat', 
        'cantopop', 'children', 'classical', 
        'comedy', 'dance', 'death-metal', 'detroit-techno', 
        'disney', 'dub', 'edm', 'eletronic', 'folk', 'fench', 
        'garage', 'gospel', 'grindcore', 'grunge', 'happy', 
        'hardcore', 'heavy-metal', 'honky-tonky', 'idm', 'indie', 
        'industrial', 'j-dance', 'j-pop', 'jazz', 'kids', 'latino', 
        'mandopop', 'metalcore', 'mpb', 'opera', 'árty', 'pop', 'power-pop', 
        'psych-pop', 'punk-rock', 'regge', 'rock', 'rockabilly', 
        'sad', 'samba', 'show-tunes', 'ska', 'songwriter', 'spanish', 
        'swedish', 'tango', 'trance', 'turkish',
    ))



st.sidebar.subheader('Gráfico de Barra Horizontal 3: ')

eixo_x_barra_horizontal_4 = st.sidebar.selectbox(
    'Eixo X - gráfico de barra horizontal 3', (
        'popularidade',
        'duracao(min)',
        'explicita' ,
        'dancabilidade',
        'energia',
        'altura(db)',
        'falada',
        'acustica',
        'instrumental',
        'ao vivo',
        'valencia',
        'bpm',
        'compasso',
    ))


eixo_y_barra_horizontal_4 = st.sidebar.selectbox(
    'Eixo Y - gráfico de barra horizontal 3', (
        'acoustic', 'alt-rock', 'ambient', 
        'black-metal', 'blues', 'breakbeat', 
        'cantopop', 'children', 'classical', 
        'comedy', 'dance', 'death-metal', 'detroit-techno', 
        'disney', 'dub', 'edm', 'eletronic', 'folk', 'fench', 
        'garage', 'gospel', 'grindcore', 'grunge', 'happy', 
        'hardcore', 'heavy-metal', 'honky-tonky', 'idm', 'indie', 
        'industrial', 'j-dance', 'j-pop', 'jazz', 'kids', 'latino', 
        'mandopop', 'metalcore', 'mpb', 'opera', 'árty', 'pop', 'power-pop', 
        'psych-pop', 'punk-rock', 'regge', 'rock', 'rockabilly', 
        'sad', 'samba', 'show-tunes', 'ska', 'songwriter', 'spanish', 
        'swedish', 'tango', 'trance', 'turkish',
    ))

st.sidebar.subheader('Gráfico de Caixa (Boxplot): ')

coluna_diagrama_de_caixa = st.sidebar.selectbox(
    'Coluna - gráfico de caixa', (
        'popularidade',
        'duracao(min)',
        'explicita' ,
        'dancabilidade',
        'energia',
        'altura(db)',
        'falada',
        'acustica',
        'instrumental',
        'ao vivo',
        'valencia',
        'bpm',
        'compasso',
    ))

# Gráfico de Barra Horizontal
# figsize=(horizontal, vertical) respectivamente
# fig, ax = plt.subplots(figsize=(10, 5))
# genero = ['Comédia', 'Ação', 'Romance', 'Drama', 'SciFi']
# qtde = [30, 20, 40, 15, 25]

# ax.barh(genero, qtde, height=1, color=['purple', 'green'], edgecolor='white', linewidth=3)
# ax.set_title('Gráfico de Filmes', fontsize='16')
# ax.set_xlabel('Notas', fontsize='12')
# ax.set_ylabel('Gêneros', fontsize='12')
# st.pyplot(fig)

# Gráfico de Barra Vertical
# fig, ax = plt.subplots()
# genero = ['Comédia', 'Ação', 'Romance', 'Drama', 'SciFi']
# qtde = [30, 20, 40, 15, 25]

# ax.bar(genero, qtde, width=1, color=['purple', 'green'], edgecolor='white', linewidth=3)
# st.pyplot(fig)

# Gráfico de Linha
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 10, 50]
# fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
# ax.plot(x, y)
# st.pyplot(fig)


st.subheader('• Gráfico de Barra Horizontal 1')
st.caption('Neste gráfico é possível fazer análises com as colunas do dataset a sua escolha.')
st.bar_chart(data=nd, x=eixo_x_barra_horizontal_1, y='genero')

# st.subheader('Gráfico de Barra Horizontal 2')
# tamanho = len(nd[eixo_y_barra_horizontal_2])
# eixo_y = []
# eixo_x = []
# for i in range(10):
    # z = random.randint(0, tamanho-1)
    # eixo_y.append(nd[eixo_y_barra_horizontal_2][z])
    # eixo_x.append(nd[eixo_x_barra_horizontal_2][z])

# plt.rcdefaults()
# fig, ax = plt.subplots()
# ax.barh(eixo_y, eixo_x)
# st.pyplot(fig)

# eixo_y

# tamanho


st.subheader('• Gráfico de Barra Horizontal 2')
st.caption('''Neste gráfico é possível escolher um gênero (eixo Y) e ele lhe retornará os artistas mais famosos do gênero escolhido.
           E aprtir disto é possível fazer análises com as outras colunas a sua escolha do datset (eixo X).''')

genre = nd.loc[nd['genero']==eixo_y_barra_horizontal_3]
genre_10 = genre.sort_values(by='popularidade', ascending=False).head(10)
artist_10 = genre_10['artistas']

eixo_x3 = []
for i in range(10):

    z = random.randint(0, 10-1)
    eixo_x3.append(nd[eixo_x_barra_horizontal_3][z])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(artist_10, eixo_x3)
st.pyplot(fig)

artist_10

st.subheader('• Gráfico de Barra Horizontal 3')
st.caption('''Neste gráfico é possível escolher um gênero (eixo Y) e ele lhe retornará as músicas mais famosas do gênero escolhido.
           E aprtir disto é possível fazer análises com as outras colunas a sua escolha do datset (eixo X).''')

name = nd.loc[nd['genero']==eixo_y_barra_horizontal_4]
name_10 = genre.sort_values(by='popularidade', ascending=False).head(10)
nome_10 = name_10['nome']

eixo_x4 = []
for i in range(10):

    z = random.randint(0, 10-1)
    eixo_x4.append(nd[eixo_x_barra_horizontal_4][z])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(nome_10, eixo_x4)
st.pyplot(fig)

nome_10

st.subheader('• Gráfico de Caixa (Boxplot)')
st.caption('''Diagrama de Caixa fornece um resumo visual rápido da variabilidade de valores em um conjunto de dados. 
            Eles mostram os valores medianos, quartis superiores e inferiores, valores mínimo e máximo e 
            quaisquer valores atípicos no conjunto de dados.''')

plt.rcdefaults()
fig, ax = plt.subplots()
nd.boxplot(column=coluna_diagrama_de_caixa)
st.pyplot(fig)