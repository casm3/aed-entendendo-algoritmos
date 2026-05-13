from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    if lista1 is None:
        return lista2
    if lista2 is None:
        return lista1

    if lista1.value <= lista2.value:
        head = lista1
        lista1 = lista1.next
    else:
        head = lista2
        lista2 = lista2.next

    tail = head

    while lista1 is not None and lista2 is not None:
        if lista1.value <= lista2.value:
            tail.next = lista1
            lista1 = lista1.next
        else:
            tail.next = lista2
            lista2 = lista2.next

        tail = tail.next

    if lista1 is not None:
        tail.next = lista1
    else:
        tail.next = lista2

    return head
