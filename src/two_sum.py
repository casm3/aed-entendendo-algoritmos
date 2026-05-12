from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    
    for m in range(len(array)):
        for l in range(m + 1, len(array)):
            if array[m] + array[l] == target:
                return(m,l)
    return(-1,-1)
