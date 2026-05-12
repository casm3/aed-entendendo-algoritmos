from src.my_array import MyArray


def two_sum(arr: MyArray, target: int) -> tuple[int, int]:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr.get(i) + arr.get(j) == target:
                return (i, j)
    return (-1, -1)
