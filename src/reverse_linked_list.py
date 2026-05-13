from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    ant = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = ant
        ant = current
        current = next_node

    return ant
    raise NotImplementedError
