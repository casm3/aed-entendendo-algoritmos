from src.my_node import MyNode

def kth_to_last(head: MyNode, k: int) -> int:
    primeiro = head
    segundo = head

    for _ in range(k):
        if segundo is None:
            return -1
        segundo = segundo.next

    while segundo is not None:
        primeiro = primeiro.next
        segundo = segundo.next

    
    return primeiro.value if primeiro is not None else -1
