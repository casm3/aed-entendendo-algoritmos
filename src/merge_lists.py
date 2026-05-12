from src.my_node import MyNode


def merge_lists(lista1: MyNode, lista2: MyNode) -> MyNode:
    sla = MyNode(0) 
    atual = sla
    while lista1 and lista2:
        if lista1.value <= lista2.value:
            atual.next = lista1
            lista1 = lista1.next
        
        else:
            atual.next = lista2
            lista2 = lista2.next

        atual = atual.next
    
    if lista1:
        atual.next = lista1
    if lista2:
        atual.next = lista2
    
    return sla.next
        