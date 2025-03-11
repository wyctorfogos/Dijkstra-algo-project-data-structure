
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import ListaEncadeada
import Queue, PriorityQueue
# models/dijkstra.py

# models/dijkstra.py
class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo  # Grafo representado como um dicionário
        self.distancias = {}  # Distâncias mínimas dos nós
        self.anterior = {}  # Caminhos anteriores
        self.nos_visitados = set()  # Nós já visitados

    def calcular(self, origem):
        # Inicializa as distâncias
        for no in self.grafo:
            self.distancias[no] = float('inf')
            self.anterior[no] = None
        self.distancias[origem] = 0

        # Fila de prioridade (heapq)
        fila = PriorityQueue.QueueWithPriority()
        fila.add_element(origem, 0)  # Origem com distância 0

        while not fila.is_empty():
            no_atual = fila.pop()  

            if no_atual in self.nos_visitados:
                continue

            self.nos_visitados.add(no_atual)

            for vizinho, custo in self.grafo[no_atual].items():
                nova_distancia = self.distancias[no_atual] + custo

                if nova_distancia < self.distancias[vizinho]:
                    self.distancias[vizinho] = nova_distancia
                    self.anterior[vizinho] = no_atual
                    fila.add_element(vizinho, nova_distancia)
        
    def reconstruir_caminho(self, destino):
        # O caminho será salvo em uma lista encadeada
        caminho = ListaEncadeada.ListaEncadeada()
        atual = destino
        while atual is not None:
            caminho.adicionar(atual, self.distancias[atual])
            atual = self.anterior[atual]
        
        # Extrai os nós da lista encadeada para uma lista normal
        lista_caminho = []
        temp = caminho.no_root
        while temp:
            lista_caminho.append(temp.no)
            temp = temp.proximo
        
        return lista_caminho