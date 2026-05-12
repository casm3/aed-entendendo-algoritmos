from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if k == 0:
        return -1

    leader = head
    follower = head

    for _ in range(k):
        if leader is None:
            return -1
        leader = leader.next

    while leader is not None:
        leader = leader.next
        follower = follower.next

    return follower.value
