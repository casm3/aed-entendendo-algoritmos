from src.my_array import MyArray

def quick_sort(array: MyArray, inicio=0, fim=None) -> MyArray:
    
    if fim is None:
        fim = len(array) - 1

    if inicio >= fim:
        return array

    pivo = array[fim] 
    i = inicio       
    
    for j in range(inicio, fim):

        if array[j] < pivo:
            array[i], array[j] = array[j], array[i]
            i += 1
            
    array[i], array[fim] = array[fim], array[i]

    quick_sort(array, inicio, i - 1)
    quick_sort(array, i + 1, fim)

    return array