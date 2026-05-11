from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    if not lista1:
        return lista2
    if not lista2:
        return lista1
    
    if lista1.value <= lista2.value:
        head = lista1
        lista1 = lista1.next
    else:
        head = lista2
        lista2 = lista2.next 
    inicial = head

    while lista1 and lista2:
        if lista1.value <= lista2.value:
            inicial.next = lista1
            lista1 = lista1.next
        else:
            inicial.next = lista2
            lista2 = lista2.next

        inicial = inicial.next
    
    if lista1:
        inicial.next = lista1
    else:
        inicial.next = lista2

    return head