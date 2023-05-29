def menor_diferenca(array):
    array.sort()  # Ordena o array em ordem crescente
    menor_dif = float('inf')  # Inicializa a menor diferença como infinito
    pares = []  # Lista para armazenar os pares com a menor diferença

    # Percorre o array e verifica as diferenças entre os elementos adjacentes
    for i in range(len(array) - 1):
        dif = abs(array[i] - array[i + 1])

        if dif < menor_dif:  # Se encontrou uma diferença menor
            menor_dif = dif  # Atualiza a menor diferença
            pares = [(array[i], array[i + 1])]  # Reinicia a lista com o novo par
        elif dif == menor_dif:  # Se encontrou uma diferença igual à menor diferença
            pares.append((array[i], array[i + 1]))  # Adiciona o novo par à lista de pares

    return pares
