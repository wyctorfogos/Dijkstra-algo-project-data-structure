
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import ListaEncadeada
import Queue
# models/dijkstra.py
import heapq  # Necessário para usar a fila de prioridade

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo  # Grafo representado como um dicionário
        self.distancias = {}  # Distâncias mínimas dos nós
        self.anterior = {}  # Caminhos anteriores
        self.nos_visitados = set()  # Nó já visitado

    def calcular(self, origem):
        for no in self.grafo:
            self.distancias[no] = float('inf')  # Define todas as distâncias como infinitas
            self.anterior[no] = None  # Nenhum caminho anterior ainda
        self.distancias[origem] = 0

        fila = heapq.heapify([origem])  # Inicializa a fila com prioridade

        while fila:  # Enquanto houver elementos na fila
            no_atual = heapq.heappop(fila)  # Pega o nó com menor distância
            
            if no_atual in self.nos_visitados:
                continue  # Se já visitado, salta para próxima

            self.nos_visitados.add(no_atual)

            for vizinho, custo in self.grafo[no_atual].items():  # Processa cada vizinho
                nova_distancia = self.distancias[no_atual] + custo
                
                if nova_distancia < self.distancias[vizinho]:
                    self.distancias[vizinho] = nova_distancia
                    self.anterior[vizinho] = no_atual
                    
                    # Atualiza a fila com a nova distância
                    heapq.heappush(fila, (nova_distancia, vizinho))
                    
        return self.distancias

    def reconstruir_caminho(self, destino):
        # O caminho a ser feito vai ser salvo, as sequências de nos, entre os dados
        caminho = ListaEncadeada.ListaEncadeada()
        atual = destino
        while atual is not None:
            caminho.adicionar(atual, self.distancias[atual])
            atual = self.anterior.get(atual, None)  # Verifica se o predecessor existe

        # Extração dos nos da lista encadeada para uma lista normal
        lista_caminho = []
        temp = caminho.no_root
        while temp:
            lista_caminho.append(temp.no)
            temp = temp.proximo
        
        return lista_caminho
