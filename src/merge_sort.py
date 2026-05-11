from src.my_array import MyArray


def merge_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array
    
    meio_array = len(array) // 2
    esquerda = array[:meio_array]
    direita = array[meio_array:]

    ordenar_esquerda = merge_sort(esquerda)
    ordenar_direita = merge_sort(direita)

    return intercalar(ordenar_esquerda,ordenar_direita)

def intercalar(esquerda, direita):
    resultado_final = []

    m = 0
    l = 0

    while m <= len(esquerda) and l <= len(direita):
        if esquerda[m] <= direita[l]:
            resultado_final.append(esquerda)
            m += 1
        else:
            resultado_final.append(direita)
            l += 1

    resultado_final.extend(esquerda[m:])
    resultado_final.extend(direita[:l])