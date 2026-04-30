from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if head is None or k <= 0:
        return -1

    ponteiro_rapido = head
    ponteiro_lento = head

    for _ in range(k):
        if ponteiro_rapido is None:
            return -1
        ponteiro_rapido = ponteiro_rapido.next

    while ponteiro_rapido is not None:
        ponteiro_rapido = ponteiro_rapido.next
        ponteiro_lento = ponteiro_lento.next

    return ponteiro_lento.value
