from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if head is None or k <= 0:
        return -1
    
    lider = head
    seguidor = head

    for _ in range(k-1):
        lider = lider.next
        if lider is None:
            return -1

    while lider.next is not None:
        lider = lider.next
        seguidor = seguidor.next

    return seguidor.value