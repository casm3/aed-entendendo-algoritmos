from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    if head is None:
        return None

    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head
