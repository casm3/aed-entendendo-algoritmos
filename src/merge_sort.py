def merge_sort(array):
    if len(array) <= 1:
        if len(array) == 1:
            return [array[0]]
        return []
    meio = len(array) // 2

    esquerda = [array[i] for i in range(meio)]
    direita = [array[i] for i in range(meio, len(array))]

    esquerda_ordem = merge_sort(esquerda)
    direita_ordem = merge_sort(direita)

    return merge(esquerda_ordem, direita_ordem)


def merge(esquerda, direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado