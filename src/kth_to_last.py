from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if not head or k <= 0:
        return -1

    lento = head
    rapido = head

    for i in range(k):
        if rapido is None:
            return -1
        rapido = rapido.next

    while rapido is not None:
        lento = lento.next
        rapido = rapido.next

    return lento.value
