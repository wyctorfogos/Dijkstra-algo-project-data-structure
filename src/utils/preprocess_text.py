# utils/preprocess_text.py

class PROCESSAMENTO_DE_TEXTO:
    @staticmethod
    def ler_arquivo_de_entrada(caminho_entrada):
        with open(caminho_entrada, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        origem = linhas[0].strip()  # O primeiro nó é o ponto de origem
        grafo = {}

        for linha in linhas[1:]:
            dados = linha.strip().split(', ')
            no_atual = dados[0]
            distancias = list(map(float, dados[1:]))  # Converte as distâncias para float
            
            vizinhos = {}
            for i, dist in enumerate(distancias):
                if dist > 0:  # Ignora distâncias 0 (sem conexão direta)
                    vizinhos[f'node_{i}'] = dist

            grafo[no_atual] = vizinhos

        return origem, grafo

    @staticmethod
    def escrever_saida(caminho_saida, resultados):
        with open(caminho_saida, 'w') as arquivo:
            for resultado in resultados:
                arquivo.write(resultado + "\n")
