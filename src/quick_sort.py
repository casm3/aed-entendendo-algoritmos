from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:
    if len(array) <= 1:
        return array
    
    pivo = array[0]

    esquerda = MyArray()
    igual = MyArray()
    direita = MyArray()

    i = 0

    while i < len(array):
        if array[i] < pivo:
            esquerda.append(array[i])
        
        elif array[i] > pivo:
            direita.append(array[i])

        else:
            igual.append(array[i])

        i += 1

    esquerda = quick_sort(esquerda)
    direita = quick_sort(direita)

    resultado = MyArray()

    i = 0
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    
    i = 0

    while i < len(igual):
        resultado.append(igual[i])
        i += 1

    i = 0

    while i < len(direita):
        resultado.append(direita[i])
        i += 1

    return resultado
    
