from src.my_array import MyArray


def merge(left, right):
    result = MyArray()

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = MyArray()
    right = MyArray()

    i = 0

    while i < middle:
        left.append(arr[i])
        i += 1

    while i < len(arr):
        right.append(arr[i])
        i += 1

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
