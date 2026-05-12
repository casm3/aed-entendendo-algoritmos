from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    dir = len(array)-1 # len é tamanho, 1 a + q o index
    esq = 0
    while dir > esq:
        var_temp = array[dir]
        array[dir] = array[esq]
        array[esq] = var_temp
        dir = dir - 1
        esq = esq + 1
        
