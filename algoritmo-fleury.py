#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
#
# Fleury's Algorithm implementation, originalmente por Dawid Kulig

import copy

class FleuryException(Exception):
    def __init__(self, message):
        super(FleuryException, self).__init__(message)
        self.message = message

class Fleury:

    cor_WHITE = 'white'
    cor_GRAY  = 'gray'
    cor_BLACK = 'black'

    def __init__(self, graph):
        """
        função de atribuição a grafo dado como parâmetro
        """

        self.graph = graph

    def run(self):
        """
        função que inicia a operação do algoritmo
        """

        print('** Executando algoritmo Fleury para grafo: ** \n')
        for v in self.graph:
            print(v, ' => ', self.graph[v])
        print('\n')
        output = None
        try:
            output = self.fleury(self.graph)
        except FleuryException as message:
            print(message)

        if output:
            print('** Ciclo Euleriano encontrado: **\n')
            for v in output:
                print(v)
        print('\n** CONCLUÍDO **')

    def is_connected(self, G):
        """
        função que verifica se um determinado grafo é conectado usando o algoritmo DFS baseado em pilha
        :param G: GRAFO
        :retorna: True / False
        """

        start_node = list(G)[0]
        color = {}
        for v in G:
            color[v] = Fleury.cor_WHITE
        color[start_node] = Fleury.cor_GRAY
        S = [start_node]
        while len(S) != 0:
            u = S.pop()
            for v in G[u]:
                if color[v] == Fleury.cor_WHITE:
                    color[v] = Fleury.cor_GRAY
                    S.append(v)
                color[u] = Fleury.cor_BLACK
        return list(color.values()).count(Fleury.cor_BLACK) == len(G)

    def even_degree_nodes(self, G):
        """
        função que retorna o número de vértices pares no grafo
        Retorna: lista de vértices pares no grafo
        """

        even_degree_nodes = []
        for u in G:
            if len(G[u]) % 2 == 0:
                even_degree_nodes.append(u)
        return even_degree_nodes


    def is_eulerian(self, even_degree_odes, graph_len):
        """
        Verifica se o grafo não direcionado fornecido é um grafo Euleriano
        Retorna: true / false
        """

        return graph_len - len(even_degree_odes) == 0


    def convert_graph(self, G):
        """
        Uma função que altera a estrutura do grafo.
        Dados de entrada de amostra {0: [4, 5], 1: [2, 3, 4, 5]}
        Retorna: [(0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5)]
        """

        links = []
        for u in G:
            for v in G[u]:
                links.append((u, v))
        return links


    def fleury(self, G):
        """
        função que encontra o ciclo Euleriano em um determinado grafo
        Retorna: lista de arestas (ciclo euleriano)
        """

        edn = self.even_degree_nodes(G)
        
        # verificar se o grafo é um grafo Euleriano
        if not self.is_eulerian(edn, len(G)):
            raise FleuryException('O grafo fornecido não é um grafo Euleriano!')
        g = copy.copy(G)
        cycle = []
        
        # escolhemos qualquer vértice no grafo com um grau diferente de zero
        u = edn[0]
        while len(self.convert_graph(g)) > 0:
            current_vertex = u
            
            #for u in g[current_vertex]: # NÃO É BOM PORQUE MUDA EM PETLI
            for u in list(g[current_vertex]): # CÓPIA SEPARADA
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                # selecione uma aresta que não seja uma ponte
                # (cruzar a ponte significa não voltar para este vértice portanto, se tiver arestas não visitadas, não visitaríamos mais essas arestas e o ciclo de Euler não foi encontrado)
                bridge = not self.is_connected(g)
                if bridge:
                    # nenhuma outra escolha (aresta - ponte)
                    # lembre-se desta aresta na lista ou na pilha
                    g[current_vertex].append(u)
                    g[u].append(current_vertex)
                else:
                    break
            if bridge:
                # movemos a aresta selecionada para o próximo vértice do grafo
                # remove a aresta percorrida do grafo
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                g.pop(current_vertex)
            cycle.append((current_vertex, u))
        return cycle