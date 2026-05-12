from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:

    if k <= 0:
        return -1

    fast = head
    slow = head

    for _ in range(k):

        if fast is None:
            return -1

        fast = fast.next

    while fast is not None:

        slow = slow.next
        fast = fast.next

    return slow.value