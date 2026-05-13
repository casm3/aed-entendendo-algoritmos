from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    i = 0
    j = len(array) - 1

    while i < j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

        i += 1
        j -= 1

    return array