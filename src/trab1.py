import argparse
from utils.preprocess_text import PROCESSAMENTO_DE_TEXTO
import models
from models import Queue, ListaEncadeada, AlgoritmoDjastra
import time

if __name__ == "__main__":
    # Definir argumentos do terminal
    parser = argparse.ArgumentParser(description="Cálculo de Caminhos Mínimos com o Algoritmo de Dijkstra")
    parser.add_argument('entrada', type=str, help='Caminho para o arquivo de entrada')
    parser.add_argument('saida', type=str, help='Caminho para o arquivo de saída')

    # Parse dos argumentos
    args = parser.parse_args()

    if not args.entrada:
        raise FileNotFoundError(f"Arquivo de entrada não é válido ou não encontrado! Tente novamente!")

    # Lê o arquivo de entrada
    origem, grafo = PROCESSAMENTO_DE_TEXTO.ler_arquivo_de_entrada(args.entrada)
    # Início da contagem de tempo do processamento 
    tempo_inicial = time.time()
    
    # Instancia o algoritmo de Dijkstra
    dijkstra = AlgoritmoDjastra.Dijkstra(grafo)

    # Calcula os caminhos mínimos a partir do nó de origem
    dijkstra.calcular(origem)

    # Gerando os resultados para escrever no arquivo de saída
    resultados = []
    for destino in grafo:
        caminho = dijkstra.reconstruir_caminho(destino)
        distancia = dijkstra.distancias[destino]
        resultados.append(f"SHORTEST PATH TO {destino}: {' <- '.join(caminho)} (Distance: {distancia:.2f})")

    # Escreve os resultados no arquivo de saída
    PROCESSAMENTO_DE_TEXTO.escrever_saida(args.saida, resultados)

    print("Cálculo dos caminhos mínimos concluído!")

    print(f"Tempo total de processamento: {time.time()-tempo_inicial} s\n")
