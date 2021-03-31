from posicao import definir_posicao as pos
from plotarEstadosBR import plotar
from read_shp import read_shapefile
import shapefile as shp
import numpy as np

shp_path = r'entradas/municipios_2010.shp'
sf = shp.Reader(shp_path, encoding='ISO-8859-15')
df_mun = read_shapefile(sf)

coordenadas=[]
for i in df_mun['coords']:
    x_lon = np.zeros((len(i),1))
    y_lat = np.zeros((len(i),1))
    
    for ip in range(len(i)):
        x_lon[ip], y_lat[ip] = i[ip]
        
#     x_lon = np.array_split(df1, 2, axis=1)
    x0 = round(np.mean(x_lon),2)
    y0 = round(np.mean(y_lat),2)
    coordenadas.append(np.array([x0, y0])) 

# Definição da posição de cada vértice no plano para geração da plotagem    
pos = dict(zip(list(df_mun['nome']), coordenadas))

VIZINHOS = []
# CRIAR SCRIPT PARA LER O SHAPEFILE E CRAIR LISTA DE ADJACÊNCIAS DOS MUNICÍPIOS COM FRONTEIRA
    
df_mun['vizinhos']=VIZINHOS

graus = []
for i in VIZINHOS:
    graus.append(len(i))
df['grau']=graus

## Ordenação que definirá a ordem de sequência nas listas de vértices
if titulo == 'Ordem Grau Decrescente':
    df_GrauDecrescente = df_mun.sort_values(by='grau', ascending=False)
    lista_nodes = list(df_GrauDecrescente['sigla'].unique())
elif titulo == 'Ordem Grau Crescente':
    df_GrauCrescente   = df_mun.sort_values(by='grau', ascending=True)
    lista_nodes = list(df_GrauCrescente['sigla'].unique())
else:
    lista_nodes = list(df_mun['nome'].unique())
    titulo = 'Ordem Alfabética Município'

for i in range(len(df)):
    vizinhos = dict(zip(df_mun['nome'], df_mun['vizinhos']))

lista_cores = ['yellow', 'cyan', 'green', 'magenta', 'red', 'blue', 'orange', 'gray',  
            '#00555a', '#f7d560', '#5a7d9a', '#b6b129',
            '#a1dd72', '#d49acb', '#d4a69a', '#977e93',
            '#a3cc72', '#c60acb', '#d4b22a', '#255e53',
            '#77525a', '#c7d511', '#c4c22b', '#c9b329',
            '#c8dd22', '#f75acb', '#b1a40a', '#216693',
            '#b1cd32', '#b33acb', '#c9a32b', '#925e11',
            '#c5dd39', '#d04205', '#d8a82a', '#373e29']

cores_vertices = {}
def analisar(vertice, cor):
    for vizinho in vizinhos.get(vertice): 
        cor_vizinho = cores_vertices.get(vizinho)
        print(vertice,'Tem como vizinho:', vizinho, 'Colorido com:', cor_vizinho)
        
        if cor_vizinho == cor:
            return False
    return True

def get_cor_vertice(vertice):
    for cor in lista_cores:
        print('\nAnalisando a cor', cor,'para', vertice)
        if analisar(vertice, cor):
            print('Pode-se utilizar a cor',cor,'para', vertice)
            return cor

def sequencia_cor(lista_nodes, titulo):
    for vertice in lista_nodes:
        cores_vertices[vertice] = get_cor_vertice(vertice)
        if len(cores_vertices) >1:
            print('\n',len(cores_vertices),'Estados já coloridos:',cores_vertices)
        else:
            print('\n',len(cores_vertices),'Estado já colorido:',cores_vertices)
    
    return cores_vertices

dic_cores = sequencia_cor(lista_nodes, titulo)

G = nx.Graph()
G.add_nodes_from(df_mun['nome'].unique())

lista_arestas=[]
for i in range(len(df)):
    for e in df_mun['vizinhos'][i]:
        edge = (df_mun['nome'][i], e)
        lista_arestas.append(edge)

for e in range(len(lista_arestas)):
    origem, destino = lista_arestas[e]
    G.add_edge(origem, destino)

a = list(G.nodes())

print('\n Sequência de cores: 1-Yellow, 2-Cyan, 3-Green, 4-Magenta, 5-Red, 6-Blue, 7-Orange, 8-Gray...')

cores = []
for i in range(len(a)):
    x = df_mun[df_mun['nome'] == a[i]]
    x = x.iloc[0, 2]
    c = dic_cores[x]
    cores.append(c)
    
fig = plt.figure(figsize=(10, 10)) # Creates a new figure

# vertices
nx.draw_networkx_nodes(G, 
                        pos,  
                        node_size=1800,
                        node_shape='o',
                        node_color=cores,
                        alpha=0.7)

# rótulos
nn = list(G.nodes)
dic_rotulos = {}
for i in range(len(nn)):
    x = df_mun[df_mun['nome'] == nn[i]]
    xid = x.iloc[0, 2]
    xname = x.iloc[0, 2]
    dic_rotulos[str(xid)] = xname

# arestas
nx.draw_networkx_edges(G, 
                        pos,  
                        width=2, 
                        edge_color='orange')

# rótulos
nx.draw_networkx_labels(G, 
                        pos, 
                        labels=dic_rotulos, 
                        font_size=14, 
                        font_family='sans-serif')

## Determina o número cromático do Grafo, ou seja, a menor quantidade de cores que colore o grafo conforme as restrições
cores_usadas = []
for i in cores:
    if i not in cores_usadas:
        cores_usadas.append(i)
        print(cores_usadas)
    else:
        pass

qte_cores = len(cores_usadas)

## Usando Networkx
# cores_nodes  = nx.greedy_color(G, strategy='largest_first')
# nr_cromatico = max(cores_nodes, key=cores_nodes.get)
# qte_cores    = cores_nodes[nr_cromatico]+1

print('\nQuantidade de nós coloridos:',len(cores_vertices))
# print('\nQuantidade de cores utilizadas:', qte_cores)

fig.suptitle('Grafo de Coloração dos Municípios do Brasil', fontsize=18)
plt.title('Coloração por '+titulo+', sem repetir cor para municípios adjacentes, utiliza '+str(qte_cores)+' cores')

plt.axis('off')
fig.tight_layout()
plt.savefig('saidas/GrafoColoracaoMunicipiosBR-'+titulo.replace(' ','')+'.png')

plt.show()