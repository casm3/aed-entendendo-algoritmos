from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
  """  esq = 0
    dir = len(array) - 1
    tup = [(value, index) for i, in enumerate(array)]
    array_ord = sorted(array)"""
    tam_array = len(array)
    for i in range (tam_array):
        for j in range (i + 1, tam_array):
            if array[i] + array[j] == target:# O(n^2), fazer depois uma solução otima
                return i, j
    return -1, -1        
     
    