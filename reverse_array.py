from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    inicio = 0
    fim = len(array) - 1

    while inicio < fim:
        temp = array[inicio]
        array[inicio] = array[fim]
        array[fim] = temp

        inicio += 1
        fim -= 1

    return array