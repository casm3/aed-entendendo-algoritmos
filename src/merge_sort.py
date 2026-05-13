from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = MyArray()
    for i in range(mid):
        left.append(array[i])
    right = MyArray()
    for i in range(mid, len(array)):
        right.append(array[i])

    return _merge(merge_sort(left), merge_sort(right))

def _merge(left: MyArray, right: MyArray) -> MyArray:
    merged = MyArray()
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged
