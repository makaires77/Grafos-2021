def plotar(pos,titulo):
    import matplotlib.pyplot as plt
    import networkx as nx
    import pandas as pd

    df_municipios = pd.read_csv('entradas/ibge-municipios-2019.csv', encoding='latin-1', sep=';', header=0)
    
    df_mask       = df_municipios['capital']==1
    df_capitais   = df_municipios[df_mask]
    df_capitais   = df_capitais.drop(['codigo_ibge','capital','codigo_uf'], axis = 1)
    df_capitais.columns = ['Capital [2010]','latitude','longitude']

    df_estados = pd.read_csv('entradas/IBGE_EstadosBrasil.csv', encoding='UTF-8', sep=',', header=0)
    
    df_estados = df_estados.drop(['Código','Gentílico','Governador [2019]','Área Territorial - km²; [2020]','População estimada - pessoas [2020]','Densidade demográfica - hab/km²; [2010]','Matrículas no ensino fundamental - matrículas [2018]','IDH (Índice de desenvolvimento humano) [2010]','Receitas realizadas - R$(*1000)[2017]','Rendimento mensal domiciliar per capita - R$[2020]','Total de veículos - veículos[2018]','Despesas empenhadas - R$ (*1000) [2017]'], axis=1)
    SIGLAS     = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    df_estados['sigla']=SIGLAS
    
    df = df_estados.merge(df_capitais, on='Capital [2010]') 
    
    VIZINHOS = [['AM','RO'],
            ['PE','BA','SE'],
            ['PA'],
            ['RR','AC','RO','MT','PA'],
            ['SE','AL','PE','PI','TO','GO','MG','ES'],
            ['RN','PB','PE','PI'],
            ['GO','MG'],
            ['BA','GO','MS','SP','RJ','ES'],
            ['DF','TO','MT','MS','MG','BA'],
            ['PA','TO','PI','BA'],
            ['PA','AM','RO','MS','GO','TO'],
            ['MT','PR','SP','MG','GO'],
            ['BA','GO','DF','MS','SP','RJ','ES'],
            ['AP','RR','AM','MT','TO','MA'],
            ['RN','CE','PE'],
            ['SP','MS','SC'],
            ['PB','CE','PI','BA','AL'],
            ['MA','TO','BA','PE','CE'],
            ['ES','MG','SP'],
            ['CE','PB'],
            ['SC'],
            ['AM','AC','MT'],
            ['AM','PA'],
            ['PR','RS'],
            ['MG','MS','PR','RJ'],
            ['AL','BA'],
            ['MA','PA','MT','GO','BA','PI']]
    
    df['vizinhos']=VIZINHOS

    graus = []
    for i in VIZINHOS:
        graus.append(len(i))
    df['grau']=graus
    
    ## Ordenação que definirá a ordem de sequência nas listas de vértices
    if titulo == 'Ordem Grau Decrescente':
        df_GrauDecrescente = df.sort_values(by='grau', ascending=False)
        lista_nodes = list(df_GrauDecrescente['sigla'].unique())
    elif titulo == 'Ordem Grau Crescente':
        df_GrauCrescente   = df.sort_values(by='grau', ascending=True)
        lista_nodes = list(df_GrauCrescente['sigla'].unique())
    else:
        lista_nodes = list(df['sigla'].unique())
        titulo = 'Ordem Alfabética UF'

    for i in range(len(df)):
        vizinhos = dict(zip(df['sigla'], df['vizinhos']))

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
    G.add_nodes_from(df['sigla'].unique())

    lista_arestas=[]
    for i in range(len(df)):
        for e in df['vizinhos'][i]:
            edge = (df['sigla'][i], e)
            lista_arestas.append(edge)
    
    for e in range(len(lista_arestas)):
        origem, destino = lista_arestas[e]
        G.add_edge(origem, destino)
    
    a = list(G.nodes())
    
    print('\n Sequência de cores: 1-Yellow, 2-Cyan, 3-Green, 4-Magenta, 5-Red, 6-Blue, 7-Orange, 8-Gray...')

    cores = []
    for i in range(len(a)):
        x = df[df['sigla'] == a[i]]
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
        x = df[df['sigla'] == nn[i]]
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
    
    fig.suptitle('Grafo de Coloração dos Estados do Brasil', fontsize=18)
    plt.title('Coloração por '+titulo+', sem repetir cor para estados adjacentes, utiliza '+str(qte_cores)+' cores')

    plt.axis('off')
    fig.tight_layout()
    plt.savefig('saidas/GrafoColoracaoBR-'+titulo.replace(' ','')+'.png')
    
    plt.show()

    return