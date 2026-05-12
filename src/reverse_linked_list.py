from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:

    anterior = None
    atual = head

    while atual is not None:
        posterior = atual.next

        atual.next = anterior

        anterior = atual

        atual = posterior

    return anterior