from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    dummy = MyNode(0)
    current = dummy

    while lista1 and lista2:
        if lista1.value < lista2.value:
            current.next = lista1
            lista1 = lista1.next
        else:
            current.next = lista2
            lista2 = lista2.next
        current = current.next

    if lista1:
        current.next = lista1
    elif lista2:
        current.next = lista2

    return dummy.next
