# Wyctor Fogos da Rocha
# matrícula: 2024230514

class No:
    def __init__(self, no, distancia):
        self.no = no
        self.distancia = distancia
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        # Raiz da lista (início da sequência)
        self.no_root = None  
        # Contador de elementos da lista
        self._length = 0  

    def adicionar(self, no, distancia):
        ## Adiciona um nó com base na distância
        novo_no = No(no, distancia)
        # O novo nó aponta para o antigo primeiro nó
        novo_no.proximo = self.no_root  
        # O novo nó vira a nova raiz
        self.no_root = novo_no  
        self._length += 1  

    def exibir(self):
        ## Mostra a lista encadeada.
        temp = self.no_root
        while temp:
            print(f"{temp.no} (Distância: {temp.distancia})", end=" -> ")
            temp = temp.proximo
        # Indica o fim da lista
        print("None")  

    def length(self):
        ## Retorna o tamanho da lista encadeada sem modificar `self.no_root`
        return self._length
