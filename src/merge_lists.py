from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    inicio = MyNode(0)
    fim = inicio

    while lista1 and lista2:
        if lista1.value <= lista2.value:
            fim.next = lista1

            lista1 = lista1.next

        else:
            fim.next = lista2
            lista2 = lista2.next
        fim = fim.next
    fim.next = lista1 or lista2
    return inicio.next
