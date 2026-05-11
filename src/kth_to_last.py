from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    primeiro = head
    segundo = head

    for _ in range(k):
        if primeiro is None:
            return -1

        primeiro = primeiro.next

    while primeiro is not None:
        primeiro = primeiro.next
        segundo = segundo.next

    if segundo is None:
        return -1

    return segundo.value
