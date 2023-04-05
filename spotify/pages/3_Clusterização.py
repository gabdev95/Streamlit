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
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import matplotlib.style as style

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
df = df[["acousticness","artists","danceability","duration_ms","energy","explicit","id","instrumentalness","key","liveness","loudness","mode","name","popularity","speechiness","tempo","valence","Unnamed: 0","album_name","time_signature","track_genre"]]
df = df.drop(columns = ['id', 'name','artists','album_name',"Unnamed: 0","duration_ms","popularity"])
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
st.markdown('##### 5.1.2 Converter os valores de "TRACK_GENRE" em 0 á quantidade em gêneros presentes:')
st.code('''
X = df
y = df['track_genre']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X['track_genre'] = le.fit_transform(X['track_genre'])
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
for i in range(1, 30):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state=42)
    kmeans.fit(X)
    cs.append(kmeans.inertia_)
plt.plot(range(1, 30), cs)
plt.title('Metodo do Cotovelo')
plt.xlabel('Número de Clusters')
plt.ylabel('CS')
plt.show()
''')
st.image('assets\image_cotovelo.png')
st.markdown('##### 6.1. Aplicando o método da silhueta:')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 2')
st.image('assets\silhueta_cluster_2.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 3')
st.image('assets\silhueta_cluster_3.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 4')
st.image('assets\silhueta_cluster_4.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=5, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 5')
st.image('assets\silhueta_cluster_5.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=6, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 6')
st.image('assets\silhueta_cluster_6.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=7, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 7')
st.image('assets\silhueta_cluster_7.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 8')
st.image('assets\silhueta_cluster_8.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=9, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 9')
st.image('assets\silhueta_cluster_9.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=10, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 10')
st.image('assets\silhueta_cluster_10.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=11, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 11')
st.image('assets\silhueta_cluster_11.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=12, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 12')
st.image('assets\silhueta_cluster_12.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 13')
st.image('assets\silhueta_cluster_13.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=14, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 14')
st.image('assets\silhueta_cluster_14.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=15, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 15')
st.image('assets\silhueta_cluster_15.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=17, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 16')
st.image('assets\silhueta_cluster_16.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=16, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 17')
st.image('assets\silhueta_cluster_17.png')
st.code('''
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans
model = SilhouetteVisualizer(KMeans(n_clusters=18, init='k-means++', n_init=10, max_iter=100, random_state=42))
model.fit(X)
model.show()
''')
st.markdown('##### Resultados Cluster 18')
st.image('assets\silhueta_cluster_18.png')

st.markdown('#### 7. Finalização')
st.markdown('##### 7.1. Salvando o tipo de cluster de cada coluna numa nova coluna na tabela original:')
st.code('''
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 16, random_state=42)
features = kmeans.fit_predict(X)
dados['cluster'] = features
''')
st.markdown('##### 7.2. Nova tabela:')
novo_dataset = pd.read_csv('Musicas_Cluster-2.csv')
novo_dataset
st.markdown('##### 7.3. Exibindo a quantidade de musicas em cada cluster.')
st.code('''
Número de músicas por Cluster = 
4     10547
9     10078
5      9277
6      9097
10     9048
1      8930
11     8518
14     7764
2      6671
15     6047
3      5739
7      5630
13     4973
8      4786
0      4087
12     2808
Name: cluster, dtype: int64
''')
st.markdown('##### 7.4. Exportando os dados gerados para uma planilha EXCEL.')
st.code("dados.to_excel('Musicas_Cluster-2.xlsx')")
st.markdown('##### 7.5. Exibição númerica so SCORE K de cada cluster com o método da silhueta.')
st.code('''
Silhouetter Score: 0.263
Silhouetter Score: 0.227
Silhouetter Score: 0.199
Silhouetter Score: 0.181
Silhouetter Score: 0.215
Silhouetter Score: 0.189
Silhouetter Score: 0.180
Silhouetter Score: 0.190
Silhouetter Score: 0.176
Silhouetter Score: 0.188
Silhouetter Score: 0.179
Silhouetter Score: 0.173
Silhouetter Score: 0.178
Silhouetter Score: 0.174
Silhouetter Score: 0.167
Silhouetter Score: 0.167
Silhouetter Score: 0.166
''')
