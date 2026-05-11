from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:

    # Se uma das listas estiver vazia
    if lista1 is None:
        return lista2

    if lista2 is None:
        return lista1

    # Define o início da lista resultante
    if lista1.value < lista2.value:
        head = lista1
        lista1 = lista1.next
    else:
        head = lista2
        lista2 = lista2.next

    atual = head

    # Intercala os elementos
    while lista1 is not None and lista2 is not None:

        if lista1.value < lista2.value:
            atual.next = lista1
            lista1 = lista1.next
        else:
            atual.next = lista2
            lista2 = lista2.next

        atual = atual.next

    # Conecta o restante da lista que sobrou
    if lista1 is not None:
        atual.next = lista1
    else:
        atual.next = lista2

    return head