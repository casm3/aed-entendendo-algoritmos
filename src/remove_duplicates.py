from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    if head is None or head.next is None:
        return head

    atual = head

    while atual is not None:
        comparador = atual
        while comparador.next is not None:
            if comparador.next.value == atual.value:
                comparador.next = comparador.next.next
            else:
                comparador = comparador.next
        atual = atual.next
    return head
