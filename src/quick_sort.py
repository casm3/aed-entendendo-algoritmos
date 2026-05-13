from src.my_array import MyArray


def quick_sort(array: MyArray, inicio=0, fim=None) -> MyArray:
    if fim is None:
        fim = len(array) - 1
    if inicio < fim:
        indice_pivo = particionar(array, inicio, fim)

        quick_sort(array, inicio, indice_pivo - 1)

        quick_sort(array, indice_pivo + 1, fim)

    return array


def particionar(array, inicio, fim):
    pivo = array[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[fim] = array[fim], array[i + 1]

    return i + 1