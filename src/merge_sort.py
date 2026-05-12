from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    result = []

    if len(array) <= 1: # Caso base
        return array
    
    dados = []
    for i in range (len(array)):
        dados.append(array[i]) #Pra cada elemento eu coloco ele numa lista

    meio = len(array) // 2
    esquerda = merge_sort(dados[:meio]) #Fazendo as separações recursivamente
    direita = merge_sort(dados[meio:])

    i = j = 0

    while i < len(esquerda) and j < len(direita): #Adiciona na lista global 
        if esquerda[i] <= direita[j]:
            result.append(esquerda[i])
            i += 1
        else:
            result.append(direita[j])
            j += 1

    result += esquerda[i:]
    result += direita[j:]

    return result
        
