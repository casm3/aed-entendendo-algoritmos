from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    leader = head
    follower = head

    for _ in range(k):
        if leader is None:
            return -1
        leader = leader.next

    while leader is not None:
        leader = leader.next
        follower = follower.next

    if follower is None:
        return -1

    return follower.value
