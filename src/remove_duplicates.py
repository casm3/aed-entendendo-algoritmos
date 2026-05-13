from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    if not head:
        return None
    atual = head
    while atual:
        proximo = atual

        while proximo.next:
            if atual.value == proximo.next.value:
                proximo.next = proximo.next.next
            else:
                proximo = proximo.next
        atual = atual.next
    return head