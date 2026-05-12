from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:

    if len(array) <= 1:
        return array
    dados = []

    for i in range(len(array)):
        dados.append(array[i])

    pivo = dados[0]

    menores = []
    iguais = []
    maiores = []

    for i in range(len(dados)):
        if dados[i] < pivo:
            menores.append(dados[i])
        elif dados[i] == pivo:
            iguais.append(dados[i])
        else:
            maiores.append(dados[i])      
    
    resultado = quick_sort(menores) + iguais + quick_sort(maiores)

    return resultado
