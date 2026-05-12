from src.my_array import MyArray

def reverse_array(array: MyArray) -> MyArray:
    inicio = 0
    fim = len(array)-1

    while (inicio < fim):
        temp = array[inicio] #salvo o estado do indice da esquerda antes de trocar

        array[inicio] = array[fim] # to trocando o inicio pelo fim e o fim pelo inicio
        array[fim] = temp

        inicio += 1
        fim -= 1
    #visualvente: ------><------
    return array
