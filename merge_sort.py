from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    meio = len(array) // 2

    esquerda = MyArray()
    direita = MyArray()

    for i in range(meio):
        esquerda.append(array[i])

    for i in range(meio, len(array)):
        direita.append(array[i])

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)


def merge(esquerda: MyArray, direita: MyArray) -> MyArray:
    resultado = MyArray()

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado