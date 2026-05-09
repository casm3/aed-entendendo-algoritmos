from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left_half = MyArray()
    right_half = MyArray()

    i = 0
    while i < middle:
        left_half.append(array[i])
        i += 1

    while i < len(array):
        right_half.append(array[i])
        i += 1

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left: MyArray, right: MyArray) -> MyArray:
    result = MyArray()

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
