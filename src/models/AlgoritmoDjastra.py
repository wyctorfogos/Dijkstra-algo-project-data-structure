
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import ListaEncadeada
import No
import Queue
# models/dijkstra.py

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

        fila = Queue.Queue()
        fila.enfileirar(origem)

        while not fila.esta_vazia():
            no_atual = fila.desenfileirar()
            if no_atual in self.nos_visitados:
                continue
            self.nos_visitados.add(no_atual)

            for vizinho, custo in self.grafo[no_atual].items():
                nova_distancia = self.distancias[no_atual] + custo
                if nova_distancia < self.distancias[vizinho]:
                    self.distancias[vizinho] = nova_distancia
                    self.anterior[vizinho] = no_atual
                    fila.enfileirar(vizinho)

    def reconstruir_caminho(self, destino):
        caminho = ListaEncadeada.ListaEncadeada()
        atual = destino
        while atual is not None:
            caminho.adicionar(atual, self.distancias[atual])
            atual = self.anterior[atual]
        
        # Extraímos os nós da lista encadeada para uma lista normal
        lista_caminho = []
        temp = caminho.cabeca
        while temp:
            lista_caminho.append(temp.no)
            temp = temp.proximo
        
        return lista_caminho
