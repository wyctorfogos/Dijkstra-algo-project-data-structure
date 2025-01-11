class Queue:
    def __init__(self):
        self.fila = []

    def enfileirar(self, item):
        # Adiciona um item no final da fila
        self.fila.append(item) 

    def desenfileirar(self):
        # Remove o item do início da fila
        if not self.esta_vazia():
            return self.fila.pop(0)  
        return None

    def esta_vazia(self):
        return len(self.fila) == 0
    
