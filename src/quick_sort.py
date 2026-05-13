from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp

        return i + 1

    def quicksort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_recursive(arr, low, pi - 1)
            quicksort_recursive(arr, pi + 1, high)

    quicksort_recursive(array, 0, len(array) - 1)
    return array
