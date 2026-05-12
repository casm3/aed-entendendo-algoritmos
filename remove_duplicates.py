from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    current = head
    vistos = set()
    prev = None

    while current:
        if current.value in vistos:
            prev.next = current.next
        else:
            vistos.add(current.value)
            prev = current

        current = current.next

    return head