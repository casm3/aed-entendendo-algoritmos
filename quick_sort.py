from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    lista = array.data[:]

    def quicksort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quicksort(left) + middle + quicksort(right)

    resultado = MyArray()

    for valor in quicksort(lista):
        resultado.append(valor)

    return resultado