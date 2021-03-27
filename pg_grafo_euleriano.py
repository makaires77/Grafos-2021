import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import math
from networkx.generators.classic import empty_graph, path_graph, complete_graph

G=nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3, 4, 5, 6,7,8,9,10])

#Euleriano
# G.add_edges_from([(1, 2), (1,3), (2,4), (10,6), (6,8), (3,7), (10,7), (4,5), (5,9), (8,10), (9,10)])

#Semi Euleriano
G.add_edges_from([(1, 2), (1,3), (2,4), (10,6), (6,8), (3,7), (5,7), (4,5), (8,9), (8,10), (9,4)])

#Não Euleriano
# G.add_edges_from([(1, 2), (1,3), (2,4), (10,6), (6,8), (3,7), (5,7), (4,5), (8,9), (8,10), (9,4), (3,4),(2,9)])

#verifica se todos os vértices têm grau par
edge_grau_par = 0
qtd_edge_grau_impar = 0
for node in G:
    print("Nó:"+str(node)+" grau:"+str(G.degree(node)))
    if (G.degree(node) % 2 != 0):
        edge_grau_par = 1
        qtd_edge_grau_impar+=1

if (edge_grau_par and qtd_edge_grau_impar !=2):
    print(edge_grau_par)
    print("\n"+"O Grafo não é Euleriano porque há " +str(qtd_edge_grau_impar)+" vértices com grau ímpar")
elif (edge_grau_par and qtd_edge_grau_impar ==2):
    print("\n"+"O Grafo é Semi Euleriano porque possui "+str(qtd_edge_grau_impar) +" vértices de grau ímpar")
else: 
    print("\n"+"O Grafo é Euleriano porque só tem vértices com grau par")
    

#plota o gráfico do grafo
figx = 15
figy = 10
fig, ax = plt.subplots(figsize=(figx, figy))
nx.draw_networkx(G,alpha=0.6,node_size=180,font_size=15)
plt.show()

