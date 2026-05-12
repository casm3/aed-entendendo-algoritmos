from src.my_array import MyArray


def two_sum(array: MyArray, target: int) -> tuple[int, int]:
    tamanhoLista = len(array)
    resultado = (-1,-1)

    for i in range(tamanhoLista):

        for j in range (i+1, tamanhoLista):
            if array[i] + array[j] == target:
                return (i,j)
        
    return (resultado)

