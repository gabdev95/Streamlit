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

st.title('Análises Fixas')
nd = pd.read_parquet('dataset_sem_inconsistencias.parquet')

st.caption('Os gráficos abaixo são destinados para qualquer um. São análises fixas e com descrições descritivas.')

st.subheader('• Gráfico de calor')
tabela_frequencia1 = pd.pivot_table(nd, index='genero', columns='popularidade', aggfunc='size', fill_value=0)
fig1, ax1 = plt.subplots()
sns.heatmap(tabela_frequencia1, cmap='RdYlBu', ax=ax1, vmin=1)
st.pyplot(fig1)
st.write('''
O gráfico apresentado acima é um gráfico de calor, que é também conhecido como mapa de calor, é uma visualização gráfica de dados que utiliza cores para 
representar valores numéricos de uma matriz. No gráfico acima temos no eixo Y todas os gêneros musicais presentes no dataset, e no eixo X a coluna "popularidade" e
o gráfico também apresenta ao lado direito uma barra que vai de 0 á 600, que indica a quantidade de músicas.\n
Por exemplo, se observarmos o gênero "dance" no eixo Y, percebemos que no eixo X = 0, ele tem um "quadradinho" da cor azul meio claro, olhando a barra lateral podemos 
entender que isso indica que a quantidade de músicas ali está entre 400 e 500, ou seja, o gênero dance tem entre 400 e 500 músicas com a popularidade igual a 0.\n
Porém se observamos no eixo Y o gênero "breakbeat" e obsevarmos ele na posição 44 o eixo X, podemos notar que lá temos um "quadradinho" na cor laranja claro, então
se olharmos na barra lateral isso indica que a quantidade de músicas ali presente está entre 100 e 250 (mais ou menos), ou sejo, o gênero breakbeat possui 
entre 100 e 250 (mais ou menos) músicas com popularidade = 44.
''')
         
st.subheader('• Gráfico de artistas mais famosos por gênero')
genre_AF = nd.loc[nd['genero']=='samba']
genre_10AF = genre_AF.sort_values(by='popularidade', ascending=False).head(10)
artist_10AF = genre_10AF['artistas']

eixo_x3 = []
for i in range(10):

    eixo_x3.append(nd['dancabilidade'].iloc[i])

plt.rcdefaults()
fig2, ax2 = plt.subplots()
ax2.barh(artist_10AF, eixo_x3, color='orange')
st.pyplot(fig2)
st.write('''
O gráfico apresentado acima é um gráfico que indica os artistas mais famosos do gênero "samba" que foi o escolhido para esta análise fixa. O eixo x, é a coluna "dancabilidade",
uma coluna que descreve o quanto uma música é adequada para dançar com base em uma combinação de elementos musicais, incluindo andamento, estabilidade do ritmo, força da batida 
e regularidade geral. Um valor de 0.0 é menos dançável e 1.0 é o mais dançável. E aqui podemos notar que todos os artistas mais famosos para o gênero "samba", apresentam 
"dancabilidade" maior que 2,5.
''')
         
genre_AF = nd.loc[nd['genero']=='samba']
genre_10AF = genre_AF.sort_values(by='popularidade', ascending=False).head(10)
artist_10AF = genre_10AF['artistas']

eixo_x3 = []
for i in range(10):

    eixo_x3.append(nd['duracao(min)'].iloc[i])

plt.rcdefaults()
fig2, ax2 = plt.subplots()
ax2.barh(artist_10AF, eixo_x3, color='orange')
st.pyplot(fig2)
st.write('''
O gráfico apresentado acima ainda é o gráfico que indica os artistas mais famosos do gênero "samba". Porém o eixo x, escolhido agora é a coluna "duracao(min)",
uma coluna que descreve a duração da músicas em minutos. E pode-se notar que os artistas mais famosos para o gênero samba todos possuem músicas com duração entre 
2 minutos e meio e 4 minutos.
''')

st.subheader('• Gráfico de músicas mais famosas por gênero')
name_maisfamosas = nd.loc[nd['genero']=='k-pop']
name_10maisfamosas = name_maisfamosas.sort_values(by='popularidade', ascending=False).head(10)
nome_10maisfamosas = name_10maisfamosas['nome']

eixo_x4 = []
for i in range(10):

    eixo_x4.append(nd['energia'].iloc[i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(nome_10maisfamosas, eixo_x4, color='pink')
st.pyplot(fig)
st.write('''
O gráfico apresentado acima ainda é o gráfico que indica as músicas mais famosas do gênero "k-pop" que foi o escolhido para esta análise fixa. O eixo x, é a coluna "energia",
uma coluna que é uma medida de 0.0 a 1.0 e representa uma medida perceptiva de intensidade e atividade. Normalmente, as faixas energéticas parecem rápidas, altas e barulhentas. 
Por exemplo, death metal tem alta energia, enquanto um prelúdio de Bach pontua baixo na escala.\n
E podemos perceber, que a maioria das músicas mais famosas apresentam energia maior que 0.3. Porém, também pode-se perceber que existem dentre as músicas mais famosas deste 
gênero músicas com energia menor que 0.2, o que pode ser considerado um outlier (um valor que se diferencia significativamente dos demais valores em um conjunto de dados. 
Em outras palavras, é um valor que "destoa" do padrão dos demais valores.), porém só é possível dizer com certeza apartir de mais análises.
''')

name_maisfamosas = nd.loc[nd['genero']=='k-pop']
name_10maisfamosas = name_maisfamosas.sort_values(by='popularidade', ascending=False).head(10)
nome_10maisfamosas = name_10maisfamosas['nome']

eixo_x4 = []
for i in range(10):

    eixo_x4.append(nd['dancabilidade'].iloc[i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(nome_10maisfamosas, eixo_x4, color='pink')
st.pyplot(fig)
st.write('''
O gráfico apresentado acima ainda é o gráfico que indica as músicas mais famosos do gênero "k-pop". Porém o eixo x, escolhido agora é a coluna "dancabilidade"
uma coluna que como já foi dito descreve o quanto uma música é adequada para dançar com base em uma combinação de elementos musicais, incluindo andamento, estabilidade do ritmo, 
força da batida e regularidade geral. Um valor de 0.0 é menos dançável e 1.0 é o mais dançável.
Observando o gráfico é notável que das dez músicas presente, nove tem a dançabilidade maior ou igual a 0.4, o que nos faz concluir que as músicas mais famosas deste gênero são
as que possuem uma dançabilidade não tão baixa como 0.3, mas sim uma dançabilidade acima ou igual a 0.4.
''')

st.subheader('• Gráfico de músicas menos famosas por gênero')
name_menosfamosas = nd.loc[nd['genero']=='mpb']
nome_10menosfamosas = name_menosfamosas.sort_values(by='popularidade', ascending=False).tail(10)
menos_famosas = nome_10menosfamosas['nome']

eixo_x5 = []

for i in range(10):

    if i == 0:
        i += 1
    eixo_x5.append(nd['energia'].iloc[-i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(menos_famosas, eixo_x5, color='brown')
st.pyplot(fig)
st.write('''
O gráfico apresentado acima ainda é um gráfico que indica as músicas menos famosos do gênero "mpb". Onde o eixo x, escolhido é a coluna "energia"
uma coluna que é uma medida de 0.0 a 1.0 e representa uma medida perceptiva de intensidade e atividade. Normalmente, as faixas energéticas parecem rápidas, altas e barulhentas. 
Por exemplo, death metal tem alta energia, enquanto um prelúdio de Bach pontua baixo na escala.\n
E observando o gráfico podemos notar que das dez músicas, seis apresentam energia maior que 0.4, enquanto as outras quatro apresentam energia menor que 0.4, podemos então inferir que 
as músicas menos famosas apresentam uma energia mais alta que 0.4.
''')

name_menosfamosas = nd.loc[nd['genero']=='mpb']
nome_10menosfamosas = name_menosfamosas.sort_values(by='popularidade', ascending=False).tail(10)
menos_famosas = nome_10menosfamosas['nome']

eixo_x5 = []

for i in range(10):

    if i == 0:
        i += 1
    eixo_x5.append(nd['dancabilidade'].iloc[-i])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(menos_famosas, eixo_x5, color='brown')
st.pyplot(fig)
st.write('''
O gráfico apresentado acima ainda é o gráfico que indica as músicas menos famosas do gênero "mpb". Porém o eixo x, escolhido agora é a coluna "dancabilidade"
uma coluna que como já foi dito descreve o quanto uma música é adequada para dançar com base em uma combinação de elementos musicais, incluindo andamento, estabilidade do ritmo, 
força da batida e regularidade geral. Um valor de 0.0 é menos dançável e 1.0 é o mais dançável.
Observando o gráfico é notável que das dez músicas presente, seis tem a dançabilidade maior que a 0.4, nos inferindo que as músicas menos famosas apresentam uma dançabilidade mais alta.
''')
