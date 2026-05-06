from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if head is None or k <= 0:
        return -1

    p1 = head
    p2 = head

    for _ in range(k):
        if p2 is None:
            return -1
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next

    return p1.value
