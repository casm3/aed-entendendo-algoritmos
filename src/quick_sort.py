from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if array is None or len(array) <= 1:
        return array
    _quick_sort_recursivo(array, 0, len(array) - 1)
    return array


def _quick_sort_recursivo(array: MyArray, inicio: int, fim: int):
    if inicio < fim:
        indice_pivo = particionar(array, inicio, fim)
        _quick_sort_recursivo(array, inicio, indice_pivo - 1)
        _quick_sort_recursivo(array, indice_pivo + 1, fim)


def particionar(array: MyArray, inicio: int, fim: int) -> int:
    pivo = array[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if array[j] <= pivo:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

    temp = array[i + 1]
    array[i + 1] = array[fim]
    array[fim] = temp

    return i + 1
