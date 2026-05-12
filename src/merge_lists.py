from src.my_node import MyNode


def merge_lists(head1: MyNode, head2: MyNode) -> MyNode:
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.value <= head2.value:
        head1.next = merge_lists(head1.next, head2)
        return head1
    else:
        head2.next = merge_lists(head1, head2.next)
        return head2
