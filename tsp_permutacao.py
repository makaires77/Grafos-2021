
# Implementação do Problema do Caixeiro Viajante em Python3
# Partindo do vértice 1, por força bruta testa as permutações de caminhos possíveis dada uma matriz de adjacência.
import numpy as np
from sys import maxsize
from itertools import permutations

def tsp_permutacao(matriz, s):

	# armazena todos os vértices em uma lista, exceto o vértice de partida
	vertices = []
	for i in range(V):
		if i != s:
			vertices.append(i)

	# armazena o peso mínimo do Cilco Hamiltoniano
	peso_minimo = maxsize
    
    # utiliza função permutação do itertools para ver os próximos passos possíveis
	permutacoes_vertices = permutations(vertices)
	
	melhor=0
	cont=1
	for i in permutacoes_vertices:
		print("Opção de caminho "+str(cont))
		# armazena o custo total percorrido do caminho
		peso_caminho = 0

		# calcula o peso k do passo atual
		k = s
		for j in i:
			print(k+1,"-",j+1,"peso:", matriz[k][j])
			peso_caminho += matriz[k][j]
			k = j
		peso_caminho += matriz[k][s]
		print(k+1,"-",1,"peso:", matriz[k][0])

		# atualiza o peso total mínimo
		
		if peso_caminho < peso_minimo:
			peso_minimo = peso_caminho
			melhor  = cont
			passos  = np.array(str(i).strip(" ").replace("(","").replace(")","").split(","))
			passos  = [int(i)+1 for i in passos]
			caminho = "[1, "+str(passos).strip("[ ]")+", 1]"
		# peso_minimo = min(peso_minimo, peso_caminho)
		print("Peso Caminho atual: ",peso_caminho, "| Peso Mínimo achado: ",peso_minimo,"\n")
		cont+=1

	return peso_minimo, cont-1, melhor, caminho


# Chamada da função
if __name__ == "__main__":

	# matriz de adjacência que representa o grafo do hexagono completo
	# matriz=[[ 0, 18, 17, 23, 12, 19], 
    #         [18,  0, 26, 31, 20, 30],
    #         [17, 26,  0, 16, 11,  9],
    #         [23, 31, 16,  0, 17, 19], 
    #         [12, 20, 11, 17,  0, 14],
    #         [19, 30,  9, 19, 14,  0]]
    
	# matriz de adjacência que representa o grafo das 4 regiões do CE
	matriz=[[     0,  30, np.inf, 40], 
            [    30,   0,     26, 25],
            [np.inf,  26,      0, 17],
            [    40,  25,     17,  0]]

	# # matriz de adjacência que representa o grafo das 7 regiões do CE
	# matriz=[[     0,     30, np.inf,     40, np.inf, np.inf, np.inf], 
    #         [    30,      0,     26,     25,      5, np.inf, np.inf],
    #         [np.inf,      5,      0, np.inf, np.inf, np.inf, np.inf],
    #         [    40,     25,     17,      0, np.inf,     11,     20],
    #         [np.inf,      5, np.inf, np.inf,      0, np.inf, np.inf],
	# 		[np.inf, np.inf,      8,     11, np.inf,      0,      6],
    #         [np.inf, np.inf, np.inf,     20, np.inf,      6,      0]]
    
	V = len(matriz)
	s = 0

	peso, iterações, melhor, caminho = tsp_permutacao(matriz, s)
	print("-"*90)
	print(peso,"de Peso Total Mínimo encontrado, em",iterações,"iterações")
	print("Melhor caminho", caminho,"na iteração", melhor)
	print("-"*90)