import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import random
import seaborn as sns

st.set_page_config(
    page_title='Análises', 
    page_icon='assets\logo.png', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

st.title('Análises Interativas')
nd = pd.read_parquet('dataset_sem_inconsistencias.parquet')

st.caption('''
Os gráficos abaixo são os mesmos que foram exibidos nas Análises Fixas, porém aqui os mesmos são destinados para aqueles que desejam e tem certa experiência em 
manipular eixos x e y dos gráifcos para obter análises personalizadas.
''')

# Esse comando deixa o carregamento muito lento
# media = nd.mean(numeric_only=True)

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


#st.subheader('• Gráfico Geral')
#st.caption('Neste gráfico é possível fazer análises com as colunas do dataset a sua escolha.')
# eixo_x_barra_geral = st.selectbox(
#    'Eixo X - gráfico geral',
#    ('popularidade',
#        'duracao(min)',
#        'explicita' ,
#        'dancabilidade',
#        'energia',
#        'altura(db)',
#        'falada',
#        'acustica',
#        'instrumental',
#        'ao vivo',
#        'valencia',
#        'bpm',
#        'compasso',
#    ))
#st.bar_chart(data=nd, x=eixo_x_barra_geral, y='genero')

st.subheader('• Gráfico de calor')
st.write('''Um gráfico de calor, também conhecido como mapa de calor, é uma visualização gráfica de dados que utiliza cores para representar valores numéricos de uma matriz. 
Essa representação gráfica pode ser usada para identificar padrões e tendências em grandes conjuntos de dados e é especialmente útil quando há muitos dados a serem analisados.
Neste gráfico você pode fazer análises com as colunas do dataset que preferir para o eixo X, analisando sua relação com todos os gêneros presentes no dataset.''')

eixo_x_calor_geral = st.selectbox(
    'Eixo X - Gráfico de Calor',
    ('popularidade',
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

tabela_frequencia = pd.pivot_table(nd, index='genero', columns=eixo_x_calor_geral, aggfunc='size', fill_value=0)
fig, ax = plt.subplots()
sns.heatmap(tabela_frequencia, cmap='RdYlBu', ax=ax, vmin=1)
st.pyplot(fig)

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

st.subheader('• Gráfico de artistas mais famosos por gênero')
st.write('''Neste gráfico é possível escolher um gênero (eixo Y) e ele lhe retornará os artistas mais famosos do gênero escolhido.
           E a partir disto é possível fazer análises com as outras colunas a sua escolha do dataset (eixo X).''')

col1, col2 = st.columns(2)

with col1:
    eixo_x_barra_artista_musica = st.selectbox(
    'Eixo X - gráfico artistas mais famosos por gênero',
    ('popularidade',
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

with col2:
    eixo_y_barra_artista_musica = st.selectbox(
        'Eixo Y - gráfico artistas mais famosos por gênero',
        ('acoustic', 'alt-rock', 'ambient', 
            'black-metal', 'blues', 'breakbeat', 
            'cantopop', 'children', 'classical', 
            'comedy', 'dance', 'death-metal', 'detroit-techno', 
            'disney', 'dub', 'edm', 'eletronic', 'folk', 'fench', 
            'garage', 'gospel', 'grindcore', 'grunge', 'happy', 
            'hardcore', 'heavy-metal', 'honky-tonky', 'idm', 'indie', 
            'industrial', 'j-dance', 'j-pop', 'jazz', 'kids', 'k-pop', 'latino', 
            'mandopop', 'metalcore', 'mpb', 'opera', 'árty', 'pop', 'power-pop', 
            'psych-pop', 'punk-rock', 'regge', 'rock', 'rockabilly', 
            'sad', 'samba', 'show-tunes', 'ska', 'songwriter', 'spanish', 
            'swedish', 'tango', 'trance', 'turkish',
        ))


genre = nd.loc[nd['genero']==eixo_y_barra_artista_musica]
genre_10 = genre.sort_values(by='popularidade', ascending=False).head(10)
artist_10 = genre_10['artistas']

eixo_x3 = []
for i in range(10):

    eixo_x3.append(nd[eixo_x_barra_artista_musica].iloc[i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(artist_10, eixo_x3)
st.pyplot(fig)

artist_10

st.subheader('• Gráfico de músicas mais famosas por gênero')
st.write('''Neste gráfico é possível escolher um gênero (eixo Y) e ele lhe retornará as músicas mais famosas do gênero escolhido.
           E a partir disto é possível fazer análises com as outras colunas a sua escolha do dataset (eixo X).''')

col3, col4 = st.columns(2)

with col3:
    eixo_x_barra_musica = st.selectbox(
        'Eixo X - gráfico de músicas mais famosas por gênero',
        ('popularidade',
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
    
with col4:
    eixo_y_barra_musica = st.selectbox(
        'Eixo Y - gráfico de músicas mais famosas por gênero',
        ('acoustic', 'alt-rock', 'ambient', 
            'black-metal', 'blues', 'breakbeat', 
            'cantopop', 'children', 'classical', 
            'comedy', 'dance', 'death-metal', 'detroit-techno', 
            'disney', 'dub', 'edm', 'eletronic', 'folk', 'fench', 
            'garage', 'gospel', 'grindcore', 'grunge', 'happy', 
            'hardcore', 'heavy-metal', 'honky-tonky', 'idm', 'indie', 
            'industrial', 'j-dance', 'j-pop', 'jazz', 'kids', 'k-pop', 'latino', 
            'mandopop', 'metalcore', 'mpb', 'opera', 'árty', 'pop', 'power-pop', 
            'psych-pop', 'punk-rock', 'regge', 'rock', 'rockabilly', 
            'sad', 'samba', 'show-tunes', 'ska', 'songwriter', 'spanish', 
            'swedish', 'tango', 'trance', 'turkish',
        ))

name_maisfamosas = nd.loc[nd['genero']==eixo_y_barra_musica]
name_10maisfamosas = name_maisfamosas.sort_values(by='popularidade', ascending=False).head(10)
nome_10maisfamosas = name_10maisfamosas['nome']

eixo_x4 = []
for i in range(10):

    eixo_x4.append(nd[eixo_x_barra_musica].iloc[i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(nome_10maisfamosas, eixo_x4)
st.pyplot(fig)

nome_10maisfamosas

st.subheader('• Gráfico de músicas menos famosas por gênero')
st.write('''Neste gráfico é possível escolher um gênero (eixo Y) e ele lhe retornará as músicas menos famosas do gênero escolhido.
           E a partir disto é possível fazer análises com as outras colunas a sua escolha do dataset (eixo X).''')

col5, col6 = st.columns(2)

with col5:
    eixo_x_barra_musica_Nfamosa = st.selectbox(
        'Eixo X - gráfico de músicas menos famosas por gênero',
        ('popularidade',
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
    
with col6:   
    eixo_y_barra_musica_Nfamosa = st.selectbox(
        'Eixo Y - gráfico de músicas menos famosas por gênero',
        ('acoustic', 'alt-rock', 'ambient', 
            'black-metal', 'blues', 'breakbeat', 
            'cantopop', 'children', 'classical', 
            'comedy', 'dance', 'death-metal', 'detroit-techno', 
            'disney', 'dub', 'edm', 'eletronic', 'folk', 'fench', 
            'garage', 'gospel', 'grindcore', 'grunge', 'happy', 
            'hardcore', 'heavy-metal', 'honky-tonky', 'idm', 'indie', 
            'industrial', 'j-dance', 'j-pop', 'jazz', 'kids', 'k-pop', 'latino', 
            'mandopop', 'metalcore', 'mpb', 'opera', 'árty', 'pop', 'power-pop', 
            'psych-pop', 'punk-rock', 'regge', 'rock', 'rockabilly', 
            'sad', 'samba', 'show-tunes', 'ska', 'songwriter', 'spanish', 
            'swedish', 'tango', 'trance', 'turkish',
        ), key=2)

name_menosfamosas = nd.loc[nd['genero']==eixo_y_barra_musica_Nfamosa]
nome_10menosfamosas = name_menosfamosas.sort_values(by='popularidade', ascending=False).tail(10)
menos_famosas = nome_10menosfamosas['nome']

eixo_x5 = []

for i in range(10):

    if i == 0:
        i += 1
    eixo_x5.append(nd[eixo_x_barra_musica_Nfamosa].iloc[-i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(menos_famosas, eixo_x5)
st.pyplot(fig)

menos_famosas

st.subheader('• Gráfico de Caixa (Boxplot)')
st.write('''Diagrama de Caixa fornece um resumo visual rápido da variabilidade de valores em um conjunto de dados. 
            Eles mostram os valores medianos, quantos superiores e inferiores, valores mínimo e máximo e 
            quaisquer valores atípicos no conjunto de dados.''')

col7, col8 = st.columns(2)

with col7:
    coluna_diagrama_de_caixa = st.multiselect(
        'Coluna - gráfico de caixa', [
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
        ],['popularidade', 'duracao(min)'])

with col8:
    genero_boxplot = st.selectbox(
        'Gênero - gráfico de caixa',
        ('acoustic', 'alt-rock', 'ambient', 
            'black-metal', 'blues', 'breakbeat', 
            'cantopop', 'children', 'classical', 
            'comedy', 'dance', 'death-metal', 'detroit-techno', 
            'disney', 'dub', 'edm', 'eletronic', 'folk', 'fench', 
            'garage', 'gospel', 'grindcore', 'grunge', 'happy', 
            'hardcore', 'heavy-metal', 'honky-tonky', 'idm', 'indie', 
            'industrial', 'j-dance', 'j-pop', 'jazz', 'kids', 'k-pop', 'latino', 
            'mandopop', 'metalcore', 'mpb', 'opera', 'árty', 'pop', 'power-pop', 
            'psych-pop', 'punk-rock', 'regge', 'rock', 'rockabilly', 
            'sad', 'samba', 'show-tunes', 'ska', 'songwriter', 'spanish', 
            'swedish', 'tango', 'trance', 'turkish',
        ), key=3)

coluna = nd.loc[nd['genero']==genero_boxplot]
plt.rcdefaults()
fig, ax = plt.subplots()
coluna.boxplot(column=coluna_diagrama_de_caixa)
st.pyplot(fig)
