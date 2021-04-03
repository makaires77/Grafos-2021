from itertools import permutations
from numpy import Inf

def travellingSalesmanProblem(matriz, s):

    # armazena todos os vértices em uma lista, exceto o vértice de partida
    V = len(matriz)
    vertices=[]
    for i in range(V):
        if i != s:
            vertices.append(i)

    # armazena o peso mínimo do Cilco Hamiltoniano
    peso_minimo = Inf
    
    # utiliza função permutação do itertools para ver os próximos passos possíveis
    permutacoes_vertices = permutations(vertices)
    
    for i in permutacoes_vertices:

        # armazena o custo total percorrido do caminho
        peso_caminho = 0
        print(i)

        # calcula o peso k do passo atual
        k = s
        for j in i:
            peso_caminho += matriz[k][j]
            k = j
        peso_caminho += matriz[k][s]

        # atualiza o peso total mínimo
        peso_minimo = min(peso_minimo, peso_caminho)
        # print(peso_minimo)
    return peso_minimo


# Chamada da função
if __name__ == "__main__":

    # matriz que representa o grafo
    matriz=[[ 0, 18, 17, 23, 12, 19], 
            [18,  0, 26, 31, 20, 30],
            [17, 26,  0, 16, 11,  9],
            [23, 31, 16,  0, 17, 19], 
            [12, 20, 11, 17,  0, 14],
            [19, 30,  9, 19, 14,  0]]
    s = 0
    print(travellingSalesmanProblem(matriz, s))