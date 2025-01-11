# models/lista_encadeada.py
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import No

class ListaEncadeada:
    def __init__(self):
        self.no_root = None

    def adicionar(self, no, distancia):
        novo_no = No.No(no, distancia)
        if not self.no_root:
            self.no_root = novo_no
        else:
            temp = self.no_root
            while temp.proximo:
                temp = temp.proximo
            temp.proximo = novo_no

    def exibir(self):
        temp = self.no_root
        while temp:
            print(f"{temp.no} (Distância: {temp.distancia})", end=" -> ")
            temp = temp.proximo
        print("Fim")