import argparse
from utils.preprocess_text import PROCESSAMENTO_DE_TEXTO
from models import AlgoritmoDjastra, sortPaths
import time

if __name__ == "__main__":
    # Definir argumentos do terminal
    parser = argparse.ArgumentParser(description="Cálculo de Caminhos Mínimos com o Algoritmo de Dijkstra")
    parser.add_argument('entrada', type=str, help='Caminho para o arquivo de entrada')
    parser.add_argument('saida', type=str, help='Caminho para o arquivo de saída')

    # Parse dos argumentos
    args = parser.parse_args()

    if not args.entrada:
        raise FileNotFoundError("Arquivo de entrada não é válido ou não encontrado! Tente novamente!")

    # Lê o arquivo de entrada
    tempo_inicial = time.time()
    origem, grafo = PROCESSAMENTO_DE_TEXTO.ler_arquivo_de_entrada(args.entrada)
    print(f"Tempo para ler o arquivo: {(time.time()-tempo_inicial):.3f} seg\n")
    
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
        resultados.append({"destino": destino, "caminho": caminho, "distancia": distancia})

    # Ordenar os resultados antes de escrever no arquivo de saída
    resultados_ordenados = sortPaths.sort_order_nos(resultados)

    # Criar a lista formatada para escrita no arquivo
    resultados_formatados = []
    for item in resultados_ordenados:
        # Se o caminho for None ou vazio, usa mensagem alternativa
        if item['caminho'] is None or len(item['caminho']) == 0:
            caminho_str = "Sem caminho disponível"
        else:
            # Converte cada nó para string e junta com " <- "
            caminho_str = " <- ".join(map(str, item['caminho']))
        linha = f"SHORTEST PATH TO {item['destino']}: {caminho_str} (Distance: {item['distancia']:.2f})"
        resultados_formatados.append(linha)


    # Escreve os resultados no arquivo de saída
    PROCESSAMENTO_DE_TEXTO.escrever_saida(args.saida, resultados_formatados)

    print("Cálculo dos caminhos mínimos concluído!")
    print(f"Tempo total de processamento: {time.time() - tempo_inicial:.2f} s\n")
