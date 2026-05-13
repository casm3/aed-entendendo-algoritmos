from src.my_node import MyNode

def kth_to_last(head: MyNode, k: int) -> int:
    if not head or k <= 0:
        return -1
    
    inicio = head
    fim = head

    for _ in range(k):
        if not inicio:
            return -1
        inicio = inicio.next
    
    while inicio is not None:
        inicio = inicio.next
        fim = fim.next
        
    return fim.value