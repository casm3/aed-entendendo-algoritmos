from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if not head or not head.next:
        return False
    ponteiro_lento = head
    ponteiro_rapido = head

    while ponteiro_rapido is not None and ponteiro_rapido.next is not None:
        ponteiro_lento = ponteiro_lento.next
        ponteiro_rapido = ponteiro_rapido.next.next

        if ponteiro_lento == ponteiro_rapido:
            return True
    return False
