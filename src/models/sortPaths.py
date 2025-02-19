def sort_order_nos(list_of_unsorted_nos):
    """
    Ordena a lista de nós com base na chave 'distancia' em ordem crescente
    """
    n = len(list_of_unsorted_nos)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_of_unsorted_nos[j]['distancia'] > list_of_unsorted_nos[j + 1]['distancia']:
                # Troca os elementos de posição mantendo a estrutura original
                list_of_unsorted_nos[j], list_of_unsorted_nos[j + 1] = list_of_unsorted_nos[j + 1], list_of_unsorted_nos[j]

    return list_of_unsorted_nos  # Retorna a lista já ordenada
