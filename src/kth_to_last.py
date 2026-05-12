from src.my_node import MyNode

def kth_to_last(head: MyNode, k: int) -> int:

    if k <= 0:
        return -1
    
    current = head
    tamanho = 0

    while current:
        tamanho += 1
        current = current.next
    
    if k > tamanho:
        return -1

    passos = tamanho - k

    current = head
    
    for _ in range(passos):
        current = current.next

    return current.value

