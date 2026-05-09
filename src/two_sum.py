from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    i = 0

    while i < len(array):
        j = i + 1

        while j < len(array):
            if array[i] + array[j] == target:
                return (i, j)

            j += 1

        i += 1

    return (-1, -1)
    raise NotImplementedError
