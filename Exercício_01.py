#Escreva uma função que, dado um número inteiro n, retorne uma lista
#de n strings de tal forma que a string i contém i asteriscos. Por exemplo,
#para n=5, a lista retornada seria ["*", "**", "***", "****", "*****"].
#Escreva uma função que, dado um número inteiro n, retorne uma lista
#de n strings de tal forma que a string i contém i asteriscos. Por exemplo,
#para n=5, a lista retornada seria ["*", "**", "***", "****", "*****"].

def lista_asteristico(quantidade=5):
    lista = [ i * "*"  for i in range(1, quantidade+1)]
    return lista

minha_lista = lista_asteristico(20)
print(minha_lista)

