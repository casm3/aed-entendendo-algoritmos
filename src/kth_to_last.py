from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    lento = head
    rapido = head

    # Avança o ponteiro rápido k posições
    for _ in range(k):
        if rapido is None:
            return -1
        rapido = rapido.next

    # Move os dois ponteiros até o rápido chegar ao final
    while rapido is not None:
        lento = lento.next
        rapido = rapido.next

    # Se a lista estiver vazia
    if lento is None:
        return -1

    return lento.value