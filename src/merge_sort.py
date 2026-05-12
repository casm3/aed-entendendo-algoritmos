from src.my_array import MyArray

def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    
    esquerda_arr = MyArray()
    for i in range(meio):
        esquerda_arr.append(array[i])
        
    direita_arr = MyArray()
    for i in range(meio, len(array)):
        direita_arr.append(array[i])

    esquerda = merge_sort(esquerda_arr)
    direita = merge_sort(direita_arr)

    return merge(esquerda, direita)

def merge(esquerda: MyArray, direita: MyArray) -> MyArray:
    merged = MyArray()
    left_index = 0
    right_index = 0

    while left_index < len(esquerda) and right_index < len(direita):
        if esquerda[left_index] <= direita[right_index]:
            merged.append(esquerda[left_index])
            left_index += 1
        else:
            merged.append(direita[right_index])
            right_index += 1

    while left_index < len(esquerda):
        merged.append(esquerda[left_index])
        left_index += 1
        
    while right_index < len(direita):
        merged.append(direita[right_index])
        right_index += 1

    return merged