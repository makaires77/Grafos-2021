import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import math
from networkx.generators.classic import empty_graph, path_graph, complete_graph

#DEFINICAO DAS FUNCOES

def func_graph_regular (Grafo):
    #verifica se grafo é regular
    fl_graph_regular = True
    first_degree = Grafo.degree(1)
    for node in Grafo:
        if (first_degree != Grafo.degree(node)):
            fl_graph_regular = False
    return fl_graph_regular
            

def func_graph_euler (Grafo):
    #verifica se todos os vértices têm grau par
    fl_graph_euler = True

    for node in Grafo:
        if (Grafo.degree(node) % 2 != 0):
            fl_graph_euler = False
    return fl_graph_euler

def func_graph_semi_euler (Grafo):
    #verifica se tem dois vértices ímpares
    qtd_edge_grau_impar = 0

    for node in Grafo:
        if (Grafo.degree(node) % 2 != 0):
            qtd_edge_grau_impar+=1
    
    if (qtd_edge_grau_impar != 2):
        return False
    else:
        return True

# def func_path_euler(Grafo, v_orig):
#     return

# ----------------------------------------------------------------------------------
# INICIO DO PROGRAMA

G=nx.Graph()
G.add_node(1)
# G.add_nodes_from([2, 3, 4, 5, 6,7,8,9,10])

#Regular
G.add_nodes_from([2, 3, 4, 5, 6, 7, 8])
G.add_edges_from([(1, 2), (1,5), (1,4), (2,3), (3,4), (4,8), (8,5), (8,7), (6,2), (3,7), (6,7), (6,5)])

#Regular-Fleury
# G.add_nodes_from([2, 3, 4, 5, 6, 7, 8])
# G.add_edges_from([(1,2),(1,3),(1,6),(1,8),(2,5),(2,7),(2,4),(3,8),(4,7),(5,7),(7,8),(8,6)])

#Euleriano
# G.add_edges_from([(1, 2), (1,3), (2,4), (10,6), (6,8), (3,7), (10,7), (4,5), (5,9), (8,10), (9,10)])

#Semi Euleriano
# G.add_edges_from([(1, 2), (1,3), (2,4), (10,6), (6,8), (3,7), (5,7), (4,5), (8,9), (8,10), (9,4)])

#Não Euleriano
# G.add_edges_from([(1, 2), (1,3), (2,4), (10,6), (6,8), (3,7), (5,7), (4,5), (8,9), (8,10), (9,4), (3,4),(2,9)])
    
print("\n"+"=========================")


if (func_graph_regular(G)):
    print("\n"+"O Grafo é Regurar")
else:
    print("\n"+"O Grafo não é Regular")

if func_graph_euler(G):
    print("\n"+"O Grafo é Euleriano porque só tem vértices com grau par")
    # print(func_path_euler(G))
elif func_graph_semi_euler(G):
    print("\n"+"O Grafo é Semi Euleriano")
    # print(func_path_euler(G))
else:
    print("\n"+"O Grafo não é Euleriano porque há mais de dois vértices com grau ímpar")

#plota o gráfico do grafo
figx = 15
figy = 10
fig, ax = plt.subplots(figsize=(figx, figy))
nx.draw_networkx(G,alpha=0.6,node_size=180,font_size=15)
plt.show()
