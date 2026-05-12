from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    dummy = MyNode(0)
    current = dummy

    while lista1 is not None and lista2 is not None:
        if lista1.value <= lista2.value:
            current.next = lista1
            lista1 = lista1.next
        else:
            current.next = lista2
            lista2 = lista2.next

        current = current.next

    if lista1 is not None:
        current.next = lista1

    if lista2 is not None:
        current.next = lista2

    return dummy.next