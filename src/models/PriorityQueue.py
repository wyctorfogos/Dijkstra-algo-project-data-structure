import os
import sys
import heapq  # Importa a biblioteca para fila de prioridade
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# Implementação de uma fila de prioridade com a mesma interface (add, pop, esta_vazia)
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def add(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def pop(self):
        return heapq.heappop(self.elements)[1]
    
    def esta_vazia(self):
        return len(self.elements) == 0