# utils/preprocess_text.py

class PROCESSAMENTO_DE_TEXTO:
    @staticmethod
    def ler_arquivo_de_entrada(caminho_entrada):
        try:
            with open(caminho_entrada, 'r') as arquivo:
                linhas = arquivo.readlines()
            
            origem = linhas[0].strip()  # O primeiro nó é o ponto de origem
            grafo = {}

            for linha in linhas[1:]:
                dados = linha.strip().split(', ')
                no_atual = dados[0]

                # Verificar se há todos os dados são válidos
                dados_verificados =[]
                for elem in dados[1:]:
                    try:
                        valor = float(elem)  # Tenta converter para float
                    except ValueError:
                        valor = float('inf')  # Se não for número, define como infinito
                    
                    dados_verificados.append(valor)

                distancias = list(map(float, dados_verificados))  # Converte as distâncias para float
                
                vizinhos = {}
                for i, dist in enumerate(distancias):
                    if dist > 0:  # Ignora distâncias 0 (sem conexão direta)
                        vizinhos[f'node_{i}'] = dist

                grafo[no_atual] = vizinhos

            return origem, grafo
        except Exception as e:
            print(f"Erro ao tentar ler/processar o arquivo de entrada. Erro: {e}\n")
            assert FileNotFoundError

    @staticmethod
    def escrever_saida(caminho_saida, resultados):
        try:
            with open(caminho_saida, 'w') as arquivo:
                for resultado in resultados:
                    arquivo.write(resultado + "\n")
        except Exception as e:
            print(f"Erro ao escrever o texto de saida.txt. Erro:{e}")
            