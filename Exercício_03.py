#Escreva uma função que retorne todos os subconjuntos de um conjunto
#de números. Por exemplo, se a entrada for [1, 2], a saída deve ser [[], [1],
#[2], [1, 2]].

def subconjuntos(nums):
    n = len(nums)
    output = [[]]  # Inicializa a lista com um subconjunto vazio

    for num in nums:
        # Cria novos subconjuntos adicionando o número atual a cada subconjunto existente
        output += [curr + [num] for curr in output]

    return output
print(subconjuntos([1,2]))