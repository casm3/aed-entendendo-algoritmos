from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    _quick_sort(array, 0, len(array) - 1)
    return array


def _quick_sort(array: MyArray, low: int, high: int):
    if low < high:
        pivot_index = partition(array, low, high)
        _quick_sort(array, low, pivot_index - 1)
        _quick_sort(array, pivot_index + 1, high)


def partition(array: MyArray, low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[high]
    array[high] = temp
    return i + 1
