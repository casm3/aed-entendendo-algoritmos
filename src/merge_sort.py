from src.my_array import MyArray

def merge_sort(arr: MyArray) -> MyArray:
    # chama a função recursiva com índices
    return _merge_sort(arr, 0, len(arr) - 1)


def _merge_sort(arr: MyArray, inicio: int, fim: int) -> MyArray:
    if inicio >= fim:
        return arr

    meio = (inicio + fim) // 2
    _merge_sort(arr, inicio, meio)
    _merge_sort(arr, meio + 1, fim)
    _merge(arr, inicio, meio, fim)

    return arr


def _merge(arr: MyArray, inicio: int, meio: int, fim: int):

    esquerda = [arr.get(i) for i in range(inicio, meio + 1)]
    direita = [arr.get(i) for i in range(meio + 1, fim + 1)]

    i = j = 0
    k = inicio

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            arr.set(k, esquerda[i])
            i += 1
        else:
            arr.set(k, direita[j])
            j += 1
        k += 1


    while i < len(esquerda):
        arr.set(k, esquerda[i])
        i += 1
        k += 1

    while j < len(direita):
        arr.set(k, direita[j])
        j += 1
        k += 1
