from src.my_array import MyArray

def reverse_array(array: MyArray) -> MyArray:
    cont1 = 0
    cont2 = len(array) - 1

    while cont2 > cont1:
        inicio = array[cont1]
        final = array[cont2]

        array[cont1] = final
        array[cont2] = inicio

        cont1 += 1
        cont2 -= 1
    
    return array
