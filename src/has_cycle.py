from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    esquerda = head
    direita = head

    while direita is not None and direita.next is not None:
        esquerda = esquerda.next
        direita = direita.next.next

        if esquerda == direita:
            return True

    return False