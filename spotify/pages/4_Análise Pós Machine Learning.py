import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import random
import seaborn as sns

st.set_page_config(
    page_title='Análise Pós Machine Learning', 
    page_icon='assets\logo.png', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

st.title('Análise Pós Machine Learning')

st.markdown('### Pergunta 1: Quais dos dados do dataset devem ser utilizados no processo de clusterização?')
st.markdown('''O objetivo geral deste trabalho é o de desenvolver uma ferramenta de recomendação de músicas para os usuários. Com esse objetivo em mente, optou-se por colocar 
a maior parte das colunas do dataset por conter informações que julgamos serem relevantes para a recomendação da música. 
Assim, as colunas 'id', 'name','artists','album_name',"Unnamed: 0","time signature" e “track_genre” foram descartadas. as primeiras contêm identificadores únicos, já os dados 
da coluna time_signature não foram inseridas pois julgamos que os dados da coluna tempo já seriam suficientes, por fim, dados da coluna track_genre foram desconsiderados porque 
não queríamos fazer uma playlist considerando o tipo de gênero ao qual ela pertence e sim a dados mais técnicos da mesma. Todas as outras colunas foram utilizadas, 
foi feita uma transformação nos dados de “explicit” de “false” “true” para 0 e 1 e posteriormente todos os dados foram normalizados. 
''')

st.markdown('### Pergunta 2: Uma playlist criada a partir de uma música amostra, gera especificamente músicas com gêneros similares ao da música amostra?')
st.markdown('''O objetivo geral deste trabalho é o de desenvolver uma ferramenta de recomendação de músicas para os usuários. Com esse objetivo em mente, optou-se por colocar
Uma vez separadas as músicas do nosso banco de dados em clusters, foi possível fazer essa análise. A conclusão encontrada é de que uma playlist criada a partir de uma música amostra, 
não gera especificamente músicas com gêneros similares ao da música amostra. E foi utilizado do seguinte código para comprovar disto:''')
st.code('''
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization
%matplotlib inline
from sklearn.cluster import KMeans
import warnings
import plotly.express as px

warnings.filterwarnings('ignore')

dados = pd.read_excel('Musicas_Cluster.xlsx')
print("Shape of the data= ", dados.shape)
dados.head()

print('Number of data points in each cluster = \n', dados['cluster'].value_counts())

# Cluster 0
df_cluster0 = dados.loc[dados['cluster'] == 0]
print('Frequência relativa de gênero musical por cluster (0) = \n', ((df_cluster0['track_genre'].value_counts())/len(df_cluster0)*100))
dados_c0 = df_cluster0['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c0 = df_cluster0['track_genre'].value_counts().reset_index()
dados_c0 = dados_c0.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c0
px.treemap(data_frame = dados_c0, path = ['track_genre'], values = 'value_count')

# Cluster 1
df_cluster1 = dados.loc[dados['cluster'] == 1]
print('Frequência relativa de gênero musical por cluster (1) = \n', ((df_cluster1['track_genre'].value_counts())/len(df_cluster1)*100))
dados_c1 = df_cluster1['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c1 = df_cluster1['track_genre'].value_counts().reset_index()
dados_c1 = dados_c1.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c1
px.treemap(data_frame = dados_c1, path = ['track_genre'], values = 'value_count')

# Cluster 2
df_cluster2 = dados.loc[dados['cluster'] == 2]
print('Frequência relativa de gênero musical por cluster (2) = \n', ((df_cluster2['track_genre'].value_counts())/len(df_cluster2)*100))
dados_c2 = df_cluster2['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c2 = df_cluster2['track_genre'].value_counts().reset_index()
dados_c2 = dados_c2.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c2
px.treemap(data_frame = dados_c2, path = ['track_genre'], values = 'value_count')

# Cluster 3
df_cluster3 = dados.loc[dados['cluster'] == 3]
print('Frequência relativa de gênero musical por cluster (3) = \n', ((df_cluster3['track_genre'].value_counts())/len(df_cluster3)*100))
dados_c3 = df_cluster3['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c3 = df_cluster3['track_genre'].value_counts().reset_index()
dados_c3 = dados_c3.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c3
px.treemap(data_frame = dados_c3, path = ['track_genre'], values = 'value_count')
''') 
st.markdown('''A partir da contagem de vezes que cada cluster se repetia dentro da coluna cluster do nosso banco de dados, o retrato do nossa análise mostrou que existia um total de 8667 
músicas, dentro do cluster 0, no cluster 1 há um total de 44218 músicas, dentro do cluster 2 há um total de 38207 músicas e, por fim, dentro do cluster 3 há um total de 22908 
músicas: ''')

st.code('''
Number of data points in each cluster = 
1    44218
2    38207
3    22908
0     8667
Name: cluster, dtype: int64
''')

st.markdown('''Como visto no código foi feita então a separação de cada música por seu respectivo cluster, e é criada então uma nova tabela com a frequência relativa com a 
qual qual gênero aparece dentro do respectivo cluster, onde os resultados foram:
''')
st.code('''
Frequência relativa de gênero musical por cluster (0) = 
new-age          9.103496
sleep            8.480443
ambient          8.261221
classical        8.226607
study            6.888197
                   ...   
cantopop         0.011538
heavy-metal      0.011538
rock-n-roll      0.011538
gospel           0.011538
drum-and-bass    0.011538
Name: track_genre, Length: 91, dtype: float64
''')
st.code('''
Frequência relativa de gênero musical por cluster (1) = 
 power-pop    1.646388
party        1.646388
punk-rock    1.533312
punk         1.497128
j-idol       1.479036
               ...   
opera        0.092722
new-age      0.092722
romance      0.029400
classical    0.022615
tango        0.002262
Name: track_genre, Length: 114, dtype: float64
''')
st.code('''
Frequência relativa de gênero musical por cluster (2) = 
 turkish          1.719580
romance          1.413354
deep-house       1.402884
hardstyle        1.395032
drum-and-bass    1.384563
                   ...   
new-age          0.253880
sleep            0.235559
ambient          0.196299
classical        0.159657
honky-tonk       0.083754
Name: track_genre, Length: 114, dtype: float64
''')
st.code('''
Frequência relativa de gênero musical por cluster (3) = 
 honky-tonk           3.754147
jazz                 2.750131
show-tunes           2.737035
comedy               2.715209
rock-n-roll          2.710843
                       ...   
progressive-house    0.013096
breakbeat            0.008731
grindcore            0.008731
trance               0.004365
death-metal          0.004365
Name: track_genre, Length: 112, dtype: float64
''')
st.markdown('''
Dentro de seus respectivos clusters, essas músicas dos mais variados gêneros, foram agrupadas como tendo características semelhantes, sendo assim, ao utilizar uma música para 
fazer a playlist não necessariamente a música terá o mesmo gênero musical da música original.
''')