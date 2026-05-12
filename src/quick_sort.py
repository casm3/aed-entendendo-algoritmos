from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:

    if array is None or len(array) <= 1:
        return array
    
    recursao(array, 0, len(array) - 1)
    return array


def recursao(array: MyArray, comeco: int, fim: int):
    if comeco < fim:
        pivo_index = particionar(array, comeco, fim)
        recursao(array, comeco, pivo_index -1)
        recursao(array, pivo_index + 1, fim)

def particionar(array: MyArray, comeco: int, fim: int) -> int:
    pivo = array[fim]
    m = comeco -1

    for l in range(comeco, fim):
        if array[l] <= pivo:
            m += 1
            temp = array[m]
            array[m] = array[l]
            array[l] = temp
    temp = array[m + 1]
    array[m+1] = array[fim]
    array[fim] = temp
    return m + 1