from src.my_array import MyArray


def quick_sort(arr: MyArray) -> MyArray:
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: MyArray, low: int, high: int) -> None:
    if low < high:
        pivot_index = _partition(arr, low, high)
        _quick_sort(arr, low, pivot_index - 1)
        _quick_sort(arr, pivot_index + 1, high)


def _partition(arr: MyArray, low: int, high: int) -> int:
    pivot = arr.get(high)
    i = low - 1

    for j in range(low, high):
        if arr.get(j) <= pivot:
            i += 1
            temp = arr.get(i)
            arr.set(i, arr.get(j))
            arr.set(j, temp)

    temp = arr.get(i + 1)
    arr.set(i + 1, arr.get(high))
    arr.set(high, temp)

    return i + 1
