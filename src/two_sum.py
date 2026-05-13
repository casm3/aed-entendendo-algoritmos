from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    tamanho = len(array)

    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if array[i] + array[j] == target:
                return (i, j)
    return (-1, -1)