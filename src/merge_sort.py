from src.my_array import MyArray


def merge_sort(arr: MyArray) -> MyArray:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = MyArray()
    right = MyArray()

    for i in range(mid):
        left.append(arr.get(i))
    for i in range(mid, len(arr)):
        right.append(arr.get(i))

    left = merge_sort(left)
    right = merge_sort(right)

    return _merge(left, right)


def _merge(left: MyArray, right: MyArray) -> MyArray:
    result = MyArray()
    i = j = 0

    while i < len(left) and j < len(right):
        if left.get(i) <= right.get(j):
            result.append(left.get(i))
            i += 1
        else:
            result.append(right.get(j))
            j += 1

    while i < len(left):
        result.append(left.get(i))
        i += 1

    while j < len(right):
        result.append(right.get(j))
        j += 1

    return result
