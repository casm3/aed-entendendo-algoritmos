from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    n = len(array)

    if n <= 1:
        return array

    mid = n // 2

    left = MyArray()
    right = MyArray()

    for i in range(mid):
        left.append(array[i])

    for i in range(mid, n):
        right.append(array[i])

    left = merge_sort(left)
    right = merge_sort(right)

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
