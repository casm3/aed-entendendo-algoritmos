from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:
    if array is None:
        return None
    esquerda = 0
    direita = len(array) - 1

    while esquerda < direita:
        temp = array[esquerda]
        array[esquerda] = array[direita]
        array[direita] = temp
        esquerda += 1
        direita -= 1

    return array
