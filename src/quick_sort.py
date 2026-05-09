from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    pivot = array[0]

    left = MyArray()
    equal = MyArray()
    right = MyArray()

    i = 0

    while i < len(array):
        if array[i] < pivot:
            left.append(array[i])

        elif array[i] > pivot:
            right.append(array[i])

        else:
            equal.append(array[i])

        i += 1

    left = quick_sort(left)
    right = quick_sort(right)

    result = MyArray()

    i = 0
    while i < len(left):
        result.append(left[i])
        i += 1

    i = 0
    while i < len(equal):
        result.append(equal[i])
        i += 1

    i = 0
    while i < len(right):
        result.append(right[i])
        i += 1

    return result
