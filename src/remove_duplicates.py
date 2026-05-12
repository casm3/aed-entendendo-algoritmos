from src.my_node import MyNode

def remove_duplicates(head: MyNode) -> MyNode:
    atual = head

    while atual is not None:
        runner = atual
        while runner.next is not None:
            if runner.next.value == atual.value:
                # remove duplicata
                runner.next = runner.next.next
            else:
                runner = runner.next
        atual = atual.next

    return head
