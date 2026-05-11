from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    if not head:
        return None
    
    atual = head
    while atual:
        runner = atual

        while runner.next:
            if runner.next.value == atual.value:
                runner.next = runner.next.next
            else:
                runner = runner.next

        atual = atual.next

    return head 