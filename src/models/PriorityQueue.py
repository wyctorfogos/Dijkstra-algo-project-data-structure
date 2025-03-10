class Node:
    def __init__(self, priority, item):
        self.priority = priority  # Distância do nó (menor valor = maior prioridade)
        self.item = item          # Nome ou identificador do nó
        self.left = None
        self.right = None

class QueueWithPriority:
    def __init__(self):
        self.root = None

    def add_element(self, item, priority):
        """Adiciona um nó na fila de prioridade."""
        new_node = Node(priority, item)
        if not self.root:
            self.root = new_node
        else:
            self._add(self.root, new_node)

    def _add(self, current, new_node):
        """Insere um novo nó na posição correta da árvore."""
        if new_node.priority < current.priority:  # Se a prioridade for menor, insere à esquerda
            if current.left is None:
                current.left = new_node
            else:
                self._add(current.left, new_node)
        else:  # Se a prioridade for maior ou igual, insere à direita
            if current.right is None:
                current.right = new_node
            else:
                self._add(current.right, new_node)

    def pop(self):
        """Remove e retorna o nó com a menor distância (maior prioridade)."""
        if self.root is None:
            raise IndexError("A fila está vazia")

        self.root, min_node = self._remove_min(self.root)
        return min_node.item  # Retorna apenas o nome do nó removido

    def _remove_min(self, node):
        """Encontra e remove o nó com a menor prioridade (nó mais à esquerda)."""
        if node.left is None:
            return node.right, node  # Retorna o filho direito para substituir o nó removido
        node.left, min_node = self._remove_min(node.left)
        return node, min_node

    def is_empty(self):
        return self.root is None
