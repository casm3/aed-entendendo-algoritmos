from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    
    esq = 0
    dir = len(array) - 1

    while esq < dir:

        array[esq], array[dir] = array[dir], array[esq]
        esq += 1
        dir -= 1
    return array

    raise NotImplementedError
