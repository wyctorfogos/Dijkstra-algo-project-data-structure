class No:
    def __init__(self, no, distancia):
        self.no = no
        self.distancia = distancia
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.no_root = None  # Raiz da lista (início da sequência)
        self._length = 0  # Contador de elementos da lista

    def adicionar(self, no, distancia):
        ## Adiciona um nó com base na distância
        novo_no = No(no, distancia)
        # O novo nó aponta para o antigo primeiro nó
        novo_no.proximo = self.no_root  
        self.no_root = novo_no  # O novo nó vira a nova raiz
        self._length += 1  

    def exibir(self):
        ## Mostra a lista encadeada.
        temp = self.no_root
        while temp:
            print(f"{temp.no} (Distância: {temp.distancia})", end=" -> ")
            temp = temp.proximo
        print("None")  # Indica o fim da lista

    def length(self):
        ## Retorna o tamanho da lista encadeada sem modificar `self.no_root`
        return self._length  # Agora é um atributo atualizado dinamicamente
