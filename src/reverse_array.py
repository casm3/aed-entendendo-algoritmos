from src.my_array import MyArray

def reverse_array(array: MyArray) -> MyArray:
    if array is None or len(array) == 0:
        return array

    esquerda = 0
    direita = len(array) - 1

    while esquerda < direita:
        temp = array.get(esquerda)
        array.set(esquerda, array.get(direita))
        array.set(direita, temp)

        esquerda += 1
        direita -= 1

    return array
