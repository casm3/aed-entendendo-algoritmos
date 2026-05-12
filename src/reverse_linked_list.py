from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:

    previous = None
    current = head

    while current is not None:

        next_node = current.next
        current.next = previous

        previous = current
        current = next_node

    return previous
