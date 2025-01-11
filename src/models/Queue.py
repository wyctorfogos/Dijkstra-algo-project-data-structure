class Queue:
    def __init__(self):
        self.fila = []

    def add(self, item):
        # Adiciona um item no final da fila
        self.fila.append(item) 

    def pop(self):
        # Remove o item do início da fila
        if not self.esta_vazia():
            return self.fila.pop(0)  
        return None

    def esta_vazia(self):
        return self.length() == 0
    
    def length(self):
        return len(self.fila)
