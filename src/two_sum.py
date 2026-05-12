from src.my_array import MyArray


from src.my_array import MyArray

def two_sum(array: MyArray, alvo: int) -> tuple[int, int]:
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array.get(i) + array.get(j) == alvo:
                return (i, j)
    return (-1, -1)
