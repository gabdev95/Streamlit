import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
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
''')

st.code('''
Number of data points in each cluster = 
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

st.code('''
# Cluster 0
df_cluster0 = dados.loc[dados['cluster'] == 0]
print('Frequência relativa de gênero musical por cluster (0) = \n', ((df_cluster0['track_genre'].value_counts())/len(df_cluster0)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (0) = 
emo          4.893565
j-dance      4.869097
comedy       4.453144
sad          4.257402
dancehall    3.963788
               ...   
jazz         0.024468
disney       0.024468
mandopop     0.024468
opera        0.024468
romance      0.024468
Name: track_genre, Length: 98, dtype: float64
''')
st.code('''
dados_c0 = df_cluster0['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c0 = df_cluster0['track_genre'].value_counts().reset_index()
dados_c0 = dados_c0.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c0
''')
st.image('assets\musica_genero_cluster0.png')
st.code("px.treemap(data_frame = dados_c0, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 1
df_cluster1 = dados.loc[dados['cluster'] == 1]
print('Frequência relativa de gênero musical por cluster (1) = \n, ((df_cluster1['track_genre'].value_counts())/len(df_cluster1)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (1) = 
honky-tonk           4.692049
rock-n-roll          3.247480
show-tunes           3.180291
singer-songwriter    2.989922
jazz                 2.978723
                       ...   
heavy-metal          0.022396
happy                0.022396
black-metal          0.011198
detroit-techno       0.011198
minimal-techno       0.011198
Name: track_genre, Length: 104, dtype: float64
''')
st.code('''
dados_c1 = df_cluster1['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c1 = df_cluster1['track_genre'].value_counts().reset_index()
dados_c1 = dados_c1.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c1
''')
st.image('assets\musica_genero_cluster1.png')
st.code("px.treemap(data_frame = dados_c1, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 2
df_cluster2 = dados.loc[dados['cluster'] == 2]
print('Frequência relativa de gênero musical por cluster (2) = \n', ((df_cluster2['track_genre'].value_counts())/len(df_cluster2)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (2) = 
turkish      4.182282
pop          3.477739
salsa        3.432769
reggaeton    3.417778
reggae       3.312847
               ...   
iranian      0.029981
german       0.029981
garage       0.014990
hardstyle    0.014990
happy        0.014990
Name: track_genre, Length: 76, dtype: float64
''')
st.code('''
dados_c2 = df_cluster2['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c2 = df_cluster2['track_genre'].value_counts().reset_index()
dados_c2 = dados_c2.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c2
''')
st.image('assets\musica_genero_cluster2.png')
st.code("px.treemap(data_frame = dados_c2, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 3
df_cluster3 = dados.loc[dados['cluster'] == 3]
print('Frequência relativa de gênero musical por cluster (3) = \n', ((df_cluster3['track_genre'].value_counts())/len(df_cluster3)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (3) = 
romance              10.019167
tango                 7.300924
jazz                  2.962189
opera                 2.857641
turkish               2.770518
                       ...    
edm                   0.034849
detroit-techno        0.034849
progressive-house     0.017425
black-metal           0.017425
death-metal           0.017425
Name: track_genre, Length: 106, dtype: float64
''')
st.code('''
dados_c3 = df_cluster3['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c3 = df_cluster3['track_genre'].value_counts().reset_index()
dados_c3 = dados_c3.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c3
''')
st.image('assets\musica_genero_cluster3.png')
st.code("px.treemap(data_frame = dados_c3, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 4
df_cluster4 = dados.loc[dados['cluster'] == 4]
print('Frequência relativa de gênero musical por cluster (4) = \n', ((df_cluster4['track_genre'].value_counts())/len(df_cluster4)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (4) = 
party          4.048545
power-pop      3.261591
ska            3.242628
world-music    3.119370
j-idol         3.071964
                 ...   
idm            0.075851
heavy-metal    0.047407
iranian        0.037925
guitar         0.028444
tango          0.018963
Name: track_genre, Length: 69, dtype: float64
''')
st.code('''
dados_c4 = df_cluster4['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c4 = df_cluster4['track_genre'].value_counts().reset_index()
dados_c4 = dados_c4.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c4
''')
st.image('assets\musica_genero_cluster4.png')
st.code("px.treemap(data_frame = dados_c4, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 5
df_cluster5 = dados.loc[dados['cluster'] == 5]
print('Frequência relativa de gênero musical por cluster (5) = \n', ((df_cluster5['track_genre'].value_counts())/len(df_cluster5)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (5) = 
hardstyle      2.145090
house          2.112752
edm            1.789372
heavy-metal    1.724695
hip-hop        1.703137
                 ...   
sleep          0.075455
classical      0.075455
ambient        0.053897
tango          0.043117
honky-tonk     0.021559
Name: track_genre, Length: 114, dtype: float64
''')
st.code('''
dados_c5 = df_cluster5['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c5 = df_cluster5['track_genre'].value_counts().reset_index()
dados_c5 = dados_c5.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c5
''')
st.image('assets\musica_genero_cluster5.png')
st.code("px.treemap(data_frame = dados_c5, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 6
df_cluster6 = dados.loc[dados['cluster'] == 6]
print('Frequência relativa de gênero musical por cluster (6) = \n', ((df_cluster6['track_genre'].value_counts())/len(df_cluster6)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (6) = 
heavy-metal          2.660218
grunge               2.594262
country              2.561284
dubstep              2.495328
hard-rock            2.473343
                       ...   
progressive-house    0.043971
opera                0.032978
party                0.032978
psych-rock           0.021985
new-age              0.010993
Name: track_genre, Length: 83, dtype: float64
''')
st.code('''
dados_c6 = df_cluster6['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c6 = df_cluster6['track_genre'].value_counts().reset_index()
dados_c6 = dados_c6.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c6
''')
st.image('assets\musica_genero_cluster6.png')
st.code("px.treemap(data_frame = dados_c6, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 7
df_cluster7 = dados.loc[dados['cluster'] == 7]
print('Frequência relativa de gênero musical por cluster (7) = \n', ((df_cluster7['track_genre'].value_counts())/len(df_cluster7)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (7) = 
comedy      8.419183
sad         4.831261
emo         4.706927
j-dance     3.410302
hip-hop     3.285968
              ...   
jazz        0.035524
guitar      0.035524
samba       0.017762
salsa       0.017762
pop-film    0.017762
Name: track_genre, Length: 102, dtype: float64
''')
st.code('''
dados_c7 = df_cluster7['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c7 = df_cluster7['track_genre'].value_counts().reset_index()
dados_c7 = dados_c7.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c7
''')
st.image('assets\musica_genero_cluster7.png')
st.code("px.treemap(data_frame = dados_c7, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 8
df_cluster8 = dados.loc[dados['cluster'] == 8]
print('Frequência relativa de gênero musical por cluster (8) = \n', ((df_cluster8['track_genre'].value_counts())/len(df_cluster8)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (8) = 
new-age       11.053071
classical     10.823234
sleep          9.277058
piano          8.274133
ambient        8.023402
                ...    
mpb            0.020894
metal          0.020894
latin          0.020894
kids           0.020894
deep-house     0.020894
Name: track_genre, Length: 73, dtype: float64
''')
st.code('''
dados_c8 = df_cluster8['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c8 = df_cluster8['track_genre'].value_counts().reset_index()
dados_c8 = dados_c8.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c8
''')
st.image('assets\musica_genero_cluster8.png')
st.code("px.treemap(data_frame = dados_c8, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 9
df_cluster9 = dados.loc[dados['cluster'] == 9]
print('Frequência relativa de gênero musical por cluster (9) = \n', ((df_cluster9['track_genre'].value_counts())/len(df_cluster9)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (9) = 
country      3.840048
alt-rock     3.185156
grunge       3.125620
brazil       2.897400
forro        2.897400
               ...   
j-dance      0.168684
classical    0.069458
jazz         0.009923
k-pop        0.009923
latin        0.009923
Name: track_genre, Length: 67, dtype: float64
''')
st.code('''
dados_c9 = df_cluster9['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c9 = df_cluster9['track_genre'].value_counts().reset_index()
dados_c9 = dados_c9.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c9
''')
st.image('assets\musica_genero_cluster9.png')
st.code("px.treemap(data_frame = dados_c9, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 10
df_cluster10 = dados.loc[dados['cluster'] == 10]
print('Frequência relativa de gênero musical por cluster (10) = \n', ((df_cluster10['track_genre'].value_counts())/len(df_cluster10)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (10) = 
sertanejo      3.835102
punk-rock      3.724580
power-pop      3.603006
samba          3.503537
ska            3.348806
                 ...   
iranian        0.011052
heavy-metal    0.011052
grunge         0.011052
french         0.011052
folk           0.011052
Name: track_genre, Length: 78, dtype: float64
''')
st.code('''
dados_c10 = df_cluster10['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c10 = df_cluster10['track_genre'].value_counts().reset_index()
dados_c10 = dados_c10.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c10
''')
st.image('assets\musica_genero_cluster10.png')
st.code("px.treemap(data_frame = dados_c10, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 11
df_cluster11 = dados.loc[dados['cluster'] == 11]
print('Frequência relativa de gênero musical por cluster (11) = \n', ((df_cluster11['track_genre'].value_counts())/len(df_cluster11)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (11) = 
honky-tonk        4.754637
jazz              4.191125
opera             3.815450
show-tunes        3.310636
acoustic          3.158018
                    ...   
black-metal       0.035220
detroit-techno    0.035220
heavy-metal       0.023480
chicago-house     0.011740
death-metal       0.011740
Name: track_genre, Length: 105, dtype: float64
''')
st.code('''
dados_c11 = df_cluster11['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c11 = df_cluster11['track_genre'].value_counts().reset_index()
dados_c11 = dados_c11.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c11
''')
st.image('assets\musica_genero_cluster11.png')
st.code("px.treemap(data_frame = dados_c11, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 12
df_cluster12 = dados.loc[dados['cluster'] == 12]
print('Frequência relativa de gênero musical por cluster (12) = \n', ((df_cluster12['track_genre'].value_counts())/len(df_cluster12)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (12) = 
ambient        10.398860
study           9.259259
new-age         8.511396
sleep           6.481481
iranian         6.445869
                 ...    
soul            0.035613
hard-rock       0.035613
alternative     0.035613
gospel          0.035613
emo             0.035613
Name: track_genre, Length: 64, dtype: float64
''')
st.code('''
dados_c12 = df_cluster12['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c12 = df_cluster12['track_genre'].value_counts().reset_index()
dados_c12 = dados_c12.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c12
''')
st.image('assets\musica_genero_cluster12.png')
st.code("px.treemap(data_frame = dados_c12, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 13
df_cluster13 = dados.loc[dados['cluster'] == 13]
print('Frequência relativa de gênero musical por cluster (13) = \n', ((df_cluster13['track_genre'].value_counts())/len(df_cluster13)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (13) = 
minimal-techno    7.842349
detroit-techno    7.500503
chicago-house     5.027147
techno            4.906495
trance            4.805952
                    ...   
salsa             0.020109
funk              0.020109
dancehall         0.020109
classical         0.020109
cantopop          0.020109
Name: track_genre, Length: 96, dtype: float64
''')
st.code('''
dados_c13 = df_cluster13['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c13 = df_cluster13['track_genre'].value_counts().reset_index()
dados_c13 = dados_c13.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c13
''')
st.image('assets\musica_genero_cluster13.png')
st.code("px.treemap(data_frame = dados_c13, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 14
df_cluster14 = dados.loc[dados['cluster'] == 14]
print('Frequência relativa de gênero musical por cluster (14) = \n', ((df_cluster14['track_genre'].value_counts())/len(df_cluster14)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (14) = 
dance         3.129830
edm           3.052550
deep-house    3.026790
dancehall     2.962391
afrobeat      2.782071
                ...   
new-age       0.051520
jazz          0.025760
party         0.012880
piano         0.012880
pop           0.012880
Name: track_genre, Length: 80, dtype: float64
''')
st.code('''
dados_c14 = df_cluster14['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c14 = df_cluster14['track_genre'].value_counts().reset_index()
dados_c14 = dados_c14.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c14
''')
st.image('assets\musica_genero_cluster14.png')
st.code("px.treemap(data_frame = dados_c14, path = ['track_genre'], values = 'value_count')")

st.code('''
# Cluster 15
df_cluster15 = dados.loc[dados['cluster'] == 15]
print('Frequência relativa de gênero musical por cluster (15) = \n', ((df_cluster15['track_genre'].value_counts())/len(df_cluster15)*100))
''')
st.code('''
Frequência relativa de gênero musical por cluster (15) = 
minimal-techno    7.425170
detroit-techno    6.432942
grindcore         5.523400
techno            5.490326
idm               4.183893
                    ...   
dancehall         0.016537
dance             0.016537
country           0.016537
piano             0.016537
malay             0.016537
Name: track_genre, Length: 102, dtype: float64
''')
st.code('''
dados_c15 = df_cluster15['track_genre'].value_counts().rename_axis('track_genre').to_frame('value_counts')
dados_c15 = df_cluster15['track_genre'].value_counts().reset_index()
dados_c15 = dados_c15.rename(columns={'index': 'track_genre', 'track_genre': "value_count"})
dados_c15
''')
st.image('assets\musica_genero_cluster15.png')
st.code("px.treemap(data_frame = dados_c15, path = ['track_genre'], values = 'value_count')")
