import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import random
import seaborn as sns

st.set_page_config(
    page_title='Clusterização', 
    page_icon='assets\logo.png', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

st.title('Clusterização')
st.caption('''A clusterização é uma técnica de aprendizado não supervisionado usada para dividir um conjunto de dados em grupos ou clusters com base em suas características ou 
similaridades. O objetivo é encontrar padrões e estruturas nos dados sem ter um rótulo ou categoria pré-definidos. A clusterização pode ser usada em uma variedade de aplicações, 
como análise de mercado, segmentação de clientes, detecção de fraudes e agrupamento de imagens e textos. Existem vários algoritmos de clusterização, incluindo o k-means, 
o agrupamento hierárquico e o DBSCAN.'''.center(50))

st.subheader('Passo-a-passo do processo de clusterização para nosso projeto:')

st.markdown('##### 1. Fazer importação dos pacotes que serão usados:')
st.code('''
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization
%matplotlib inline
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
''')
st.markdown('##### 2. Fazer leitura e armazenamento da tabela com os dados para manipulação PYTHON/JUPYTER NOTEBOOK:')
st.code('''
dados = pd.read_csv('dataset.csv')
print("Shape of the data= ", dados.shape)
dados.head()
''')
st.markdown('##### 3. Fazer uma organização nos dados numa nova tabela, para preservar a tabela original, além de também tirar os elementos da tabela que não serão utilizados:')
st.code('''
df = dados.rename(columns={'track_name':'name' , 'track_id':'id' })
df = df[["acousticness","artists","danceability","duration_ms","energy","explicit","id","instrumentalness","key","liveness","loudness","mode","name","popularity","speechiness","tempo","valence","Unnamed: 0","album_name","time_signature"]]
df = df.drop(columns = ['id', 'name','artists','album_name',"Unnamed: 0","time_signature"])
''')
st.markdown('##### 3.5. Ao fim deste processo teremos a seguinte tabela:')
dados = pd.read_csv('dataset.csv')
print("Shape of the data= ", dados.shape)
dados.head()
df = dados.rename(columns={'track_name':'name' , 'track_id':'id' })
df = df[["acousticness","artists","danceability","duration_ms","energy","explicit","id","instrumentalness","key","liveness","loudness","mode","name","popularity","speechiness","tempo","valence","Unnamed: 0","album_name","time_signature"]]
df = df.drop(columns = ['id', 'name','artists','album_name',"Unnamed: 0","time_signature"])
df
st.markdown('##### 4. Conferir se não existem valores nulos na tabela:')
st.code('df.isnull().sum()')
st.markdown('#### 5. Normalização')
st.markdown('##### 5.1 Fazer o processo de normalização dos dados, começando por converter os valores "TRUE" e "FALSE" para "1" e "0".')
st.markdown('##### 5.1.1 Dados assim foram encontrados na coluna "EXPLICIT", por isso ela será normalizada:')
st.code('''
X = df
y = df['explicit']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['explicit'] = le.fit_transform(X['explicit'])
X.info()
''')
st.markdown('##### 5.2. Fazendo agora a normalização em todos os dados da tabela usando o método "MINMAXSCALER":')
st.code('''
cols = X.columns
from sklearn.preprocessing import MinMaxScaler
ms = MinMaxScaler()
X= ms.fit_transform(X)
X = pd.DataFrame(X, columns = [cols])
''')
st.markdown('#### 6. Métodos')
st.markdown('##### 6.1. Aplicando o método do cotovelo:')
st.code('''
from sklearn.cluster import KMeans
cs = []
for i in range(1, 12):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state=42)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 12), cs)
plt.title('Metodo do Cotovelo')
plt.xlabel('Número de Clusters')
plt.ylabel('CS')
plt.show()
''')
st.image('assets\image_cotovelo.png')
st.markdown('##### 6.1. Aplicando o método da silhueta:')
st.code('''
from sklearn.metrics import silhouette_score
range_n_clusters = [2, 3, 4, 5, 6, 7, 8,9,10,11]
silhouette_avg = []
for num_clusters in range_n_clusters:
 
 # initialise kmeans
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    cluster_labels = kmeans.labels_
 
 # silhouette score
    silhouette_avg.append(silhouette_score(X, cluster_labels))
plt.plot(range_n_clusters,silhouette_avg,"bx-")
plt.xlabel("Valores de K") 
plt.ylabel("Score da silhuetta") 
plt.title("Análise da silhuetta para o K ótimo")
plt.show()
''')
st.image('assets\silhuettaKotimo.png')
st.code('''
range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
silhouette_avg_n_clusters = []
ig, ax = plt.subplots(2, 2, figsize=(15,8))
for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    Create KMeans instance for different number of clusters
    
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
    q, mod = divmod(i, 2)
    
    Create SilhouetteVisualizer instance with KMeans instance
    Fit the visualizer
    
    visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
    visualizer.fit(X) 
''')
st.markdown('##### Resultados Cluster 2')
st.image('assets\grafico_silhueta_cluster2.png')
st.markdown('##### Resultados Cluster 3')
st.image('assets\grafico_silhueta_cluster3.png')
st.markdown('##### Resultados Cluster 4')
st.image('assets\grafico_silhueta_cluster4.png')
st.markdown('##### Resultados Cluster 5')
st.image('assets\grafico_silhueta_cluster5.png')
st.markdown('##### Resultados Cluster 6')
st.image('assets\grafico_silhueta_cluster6.png')
st.markdown('##### Resultados Cluster 7')
st.image('assets\grafico_silhueta_cluster7.png')
st.markdown('##### Resultados Cluster 8')
st.image('assets\grafico_silhueta_cluster8.png')
st.markdown('##### Resultados Cluster 9')
st.image('assets\grafico_silhueta_cluster9.png')
st.markdown('##### Resultados Cluster 10')
st.image('assets\grafico_silhueta_cluster10.png')
st.markdown('##### Resultados Cluster 11')
st.image('assets\grafico_silhueta_cluster11.png')
st.markdown('#### 7. Finalização')
st.markdown('##### 7.1. Salvando o tipo de cluster de cada coluna numa nova coluna na tabela original:')
st.code('''
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4, random_state=42)
features = kmeans.fit_predict(X)
dados['cluster'] = features
''')
st.markdown('##### 7.2. Nova tabela:')
novo_dataset = pd.read_csv('new_dataset.csv')
novo_dataset
st.markdown('##### 7.3. Exportando os dados gerados para uma planilha EXCEL.')
st.code("dados.to_excel('Musicas_Cluster.xlsx')")
