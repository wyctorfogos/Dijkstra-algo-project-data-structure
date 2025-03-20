# Wyctor Fogos da Rocha
# matrícula: 2024230514

class Node:
    def __init__(self, priority, item):
        # Distância do nó (menor valor = maior prioridade)
        self.priority = priority  
        # Nome ou identificador do nó
        self.item = item          
        self.left = None
        self.right = None

class QueueWithPriority:
    ## Fila de prioridade com o uso de uma Árvore de Busca Binárias (ABB)
    def __init__(self):
        self.root = None

    def add_element(self, item, priority):
        ## Adiciona um nó na fila junto com a prioridade
        new_node = Node(priority, item)
        # Caso não haja um nó root, ele se torna
        if not self.root:
            self.root = new_node
        # Caso contrário, apenas adiciona um novo nó
        else:
            self._add(self.root, new_node)

    def _add(self, current, new_node):
        ## Insere um novo nó sempre de modo recursivo
        if new_node.priority < current.priority:  
            if current.left is None:
                current.left = new_node
            else:
                self._add(current.left, new_node)
        # Se a prioridade for maior ou igual, insere à direita.
        else:  
            if current.right is None:
                current.right = new_node
            else:
                self._add(current.right, new_node)

    def pop(self):
        ## Remove e retorna o nó com a menor distância
        if self.root is None:
            raise IndexError("A fila está vazia")
        
        # Retorna apenas o nome do nó removido
        self.root, min_node = self._remove_min(self.root)
        return min_node.item  

    def _remove_min(self, node):
        ## Encontra e remove o nó com a menor prioridade. Nesse caso, o nó mais à esquerda.
        if node.left is None:
            # Retorna o nó filho direito para substituir o nó removido
            return node.right, node  
        node.left, min_node = self._remove_min(node.left)
        return node, min_node

    def is_empty(self):
        return self.root is None
