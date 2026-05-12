from src.my_array import MyArray

def reverse_array(array: MyArray) -> MyArray:
    #Começa com o índice 0 (primeiro elemento)
    inicio = 0 
    final = len(array) - 1 #Lê a lista e pega o último elemento 

    while inicio < final:
        #Função auxiliar para não perder os dados
        aux = array[inicio]
        #Troca de posições, inicio recebe o final, final recebe a função aux
        array[inicio] = array[final]
        array[final] = aux

        inicio += 1 
        final -= 1

    return array
    raise NotImplementedError

