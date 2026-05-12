from src.my_array import MyArray

def quick_sort(array: MyArray) -> MyArray:
    _quick_sort(array, 0, len(array) - 1)
    return array


def _quick_sort(array: MyArray, inicio: int, fim: int):
    if inicio < fim:
        pivo_index = _partition(array, inicio, fim)
        _quick_sort(array, inicio, pivo_index - 1)
        _quick_sort(array, pivo_index + 1, fim)


def _partition(array: MyArray, inicio: int, fim: int) -> int:
    pivo = array.get(fim)
    i = inicio - 1

    for j in range(inicio, fim):
        if array.get(j) <= pivo:
            i += 1
            # troca valores usando set
            temp_i = array.get(i)
            temp_j = array.get(j)
            array.set(i, temp_j)
            array.set(j, temp_i)

    # coloca o pivô na posição correta
    temp_i1 = array.get(i + 1)
    temp_fim = array.get(fim)
    array.set(i + 1, temp_fim)
    array.set(fim, temp_i1)

    return i + 1
