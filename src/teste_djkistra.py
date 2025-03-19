import argparse
import time
import numpy as np
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra
from utils.preprocess_text import PROCESSAMENTO_DE_TEXTO

def graph_dict_to_matrix(grafo):
    """
    Converte um grafo no formato de dicionário para uma matriz de adjacência.
    Para arestas inexistentes, utiliza np.inf; a diagonal recebe 0.
    Retorna a matriz no formato CSR, o mapeamento de nó -> índice e a lista ordenada de nós.
    """
    # Obter todos os nós (chaves e vizinhos)
    nodes = set(grafo.keys())
    for vizinhos in grafo.values():
        nodes.update(vizinhos.keys())
    nodes = sorted(nodes)
    node_to_idx = {node: idx for idx, node in enumerate(nodes)}
    n = len(nodes)

    # Cria matriz densa com np.inf e diagonal zerada
    M = np.full((n, n), np.inf)
    np.fill_diagonal(M, 0)

    # Preenche a matriz com os pesos das arestas
    for src, vizinhos in grafo.items():
        for dst, peso in vizinhos.items():
            i = node_to_idx[src]
            j = node_to_idx[dst]
            M[i, j] = peso

    return csr_array(M), node_to_idx, nodes

def reconstruct_path(predecessors, source_idx, dest_idx):
    """
    Reconstrói o caminho do destino até a origem utilizando o vetor de predecessores.
    Retorna a lista de índices do caminho, na ordem: [destino, ..., origem].
    Se não houver caminho, retorna lista vazia.
    """
    if dest_idx == source_idx:
        return [source_idx]

    path = []
    current = dest_idx
    while current != source_idx:
        if current == -9999:
            return []  # Sem caminho disponível
        path.append(current)
        current = predecessors[current]
    path.append(source_idx)
    return path  # A ordem é: destino <- ... <- origem

if __name__ == "__main__":
    # Definir argumentos do terminal
    parser = argparse.ArgumentParser(
        description="Cálculo de Caminhos Mínimos com Dijkstra (SciPy) para grafo direcionado em formato de dicionário"
    )
    parser.add_argument('entrada', type=str, help='Caminho para o arquivo de entrada')
    parser.add_argument('saida', type=str, help='Caminho para o arquivo de saída')
    args = parser.parse_args()

    if not args.entrada:
        raise FileNotFoundError("Arquivo de entrada não é válido ou não encontrado! Tente novamente!")

    # Lê o arquivo de entrada (deve retornar uma tupla: (origem, grafo))
    tempo_inicial = time.time()
    origem, grafo = PROCESSAMENTO_DE_TEXTO.ler_arquivo_de_entrada(args.entrada)
    print(f"Tempo para ler o arquivo: {(time.time()-tempo_inicial):.4f} seg\n")

    # Converter o dicionário para matriz de adjacência
    tempo_inicial_convert_graph = time.time()
    graph_matrix, node_to_idx, nodes_sorted = graph_dict_to_matrix(grafo)
    print(f"Tempo para converter o grafo: {(time.time()-tempo_inicial_convert_graph):.4f} seg\n")

    # Verificar se o nó de origem existe
    if origem not in node_to_idx:
        raise ValueError(f"Nó de origem '{origem}' não encontrado no grafo!")
    origem_idx = node_to_idx[origem]

    # Calcular as distâncias e os predecessores usando Dijkstra
    # Usamos directed=True para que o grafo seja tratado como direcionado
    tempo_inicial_dijkstra = time.time()
    distances, predecessors = dijkstra(
        csgraph=graph_matrix, directed=True, indices=origem_idx, return_predecessors=True
    )
    print(f"Tempo para calcular Dijkstra: {(time.time()-tempo_inicial_dijkstra):.4f} seg\n")

    # Gerar os resultados para cada destino
    resultados = []
    n = len(nodes_sorted)
    for dest_idx in range(n):
        path_indices = reconstruct_path(predecessors, origem_idx, dest_idx)
        if path_indices:
            # Converter índices para nomes dos nós
            # O caminho vem na ordem: destino <- ... <- origem (conforme esperado)
            path_nodes = [nodes_sorted[i] for i in path_indices]
        else:
            path_nodes = None
        distancia = distances[dest_idx]
        resultados.append({
            "destino": nodes_sorted[dest_idx],
            "caminho": path_nodes,
            "distancia": distancia
        })

    # Ordenar os resultados pela distância (do menor para o maior)
    resultados_ordenados = sorted(resultados, key=lambda x: x["distancia"])

    # Formatar os resultados para escrita
    resultados_formatados = []
    for item in resultados_ordenados:
        if not item["caminho"]:
            caminho_str = "Sem caminho disponível"
        else:
            caminho_str = " <- ".join(item["caminho"])
        linha = f"SHORTEST PATH TO {item['destino']}: {caminho_str} (Distance: {item['distancia']:.4f})"
        resultados_formatados.append(linha)

    # Escreve os resultados no arquivo de saída
    PROCESSAMENTO_DE_TEXTO.escrever_saida(args.saida, resultados_formatados)
    print("Cálculo dos caminhos mínimos concluído!")
    print(f"Tempo total de processamento: {time.time() - tempo_inicial:.4f} s\n")