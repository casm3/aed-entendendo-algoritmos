from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    
    n = len(array)
    
    for i in range (n):
        valor_um = array [i]

        for j in range (i + 1, n):
            valor_dois = array [j] 
            if valor_um + valor_dois == target:
                return (i, j)
    return (-1, -1)

