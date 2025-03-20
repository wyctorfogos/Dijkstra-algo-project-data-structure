# Wyctor Fogos da Rocha
# matrícula: 2024230514

class PROCESSAMENTO_DE_TEXTO:
    @staticmethod
    def ler_arquivo_de_entrada(caminho_entrada):
        try:
            with open(caminho_entrada, 'r') as arquivo:
                linhas = [linha.strip() for linha in arquivo.readlines()]

            origem = linhas[0].strip()
            # Lista de nós identificados no arquivo
            nomes_nos = []  
            grafo = {}

            # Captura os nomes dos nós e inicializa o grafo
            for linha in linhas[1:]:
                dados = linha.split(', ')
                nome_no = dados[0]
                nomes_nos.append(nome_no)
                grafo[nome_no] = {}

            # Gera automaticamente o dicionário de mapeamento para qualquer número de nós
            mapeamento = {}
            for i, no_atual in enumerate(nomes_nos):
                # Remove o próprio nó da lista
                nos_destino = nomes_nos[:i] + nomes_nos[i+1:]  
                mapeamento[no_atual] = nos_destino

            # Processamento das conexões
            for i, linha in enumerate(linhas[1:]):
                dados = linha.split(', ')
                no_atual = dados[0]
                # Valores de distância
                colunas = dados[1:]  

                if no_atual in mapeamento:
                    nos_destino = mapeamento[no_atual]
                else:
                    # Ignora nós não identificados
                    continue  

                for j, valor in enumerate(colunas):
                    try:
                        dist_aresta = float(valor)
                    except ValueError:
                        # A distância entre os nós deve ser infinita, porque não tem conexão entre eles
                        dist_aresta = float('inf')
                        pass

                    # Obtém o nó vizinho correto
                    no_vizinho = nos_destino[j]  
                    if dist_aresta>0:
                        # Conexão no_atual -> no_vizinho
                        grafo[no_atual][no_vizinho] = dist_aresta  


            return origem, grafo

        except Exception as e:
            print(f"Erro ao processar o arquivo: {e}")
            return None, {}

    @staticmethod
    def escrever_saida(caminho_saida, resultados):
        try:
            with open(caminho_saida, 'w') as arquivo:
                for resultado in resultados:
                    arquivo.write(resultado + "\n")
        except Exception as e:
            print(f"Erro ao escrever o texto de saida.txt. Erro:{e}")