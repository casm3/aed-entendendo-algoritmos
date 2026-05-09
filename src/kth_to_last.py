from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    first = head
    second = head

    count = 0

    while count < k:
        if first is None:
            return -1

        first = first.next
        count += 1

    while first is not None:
        first = first.next
        second = second.next

    if second is None:
        return -1

    return second.value
    raise NotImplementedError
