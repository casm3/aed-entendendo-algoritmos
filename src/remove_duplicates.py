from src.my_node import MyNode

def remove_duplicates(head: MyNode) -> MyNode:
    if head is None:
        return None
    
    vistos = set()
    
    atual = head
    vistos.add(atual.value)
    
    while atual.next is not None:
        if atual.next.value in vistos:
            atual.next = atual.next.next
        else:
            vistos.add(atual.next.value)
            atual = atual.next
            
    return head