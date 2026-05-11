from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    quick_sort_auxiliar(array, 0, len(array) - 1)

    return array


def quick_sort_auxiliar(array, inicio, fim):

    if inicio < fim:

        indice_pivo = particao(array, inicio, fim)

        quick_sort_auxiliar(array, inicio, indice_pivo - 1)
        quick_sort_auxiliar(array, indice_pivo + 1, fim)


def particao(array, inicio, fim):

    pivo = array[fim]

    i = inicio - 1

    for j in range(inicio, fim):

        if array[j] <= pivo:

            i += 1

            array[i], array[j] = array[j], array[i]

    array[i + 1], array[fim] = array[fim], array[i + 1]

    return i + 1