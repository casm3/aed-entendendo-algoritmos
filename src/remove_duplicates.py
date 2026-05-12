from src.my_node import MyNode


def remove_duplicates(head):
    current = head

    while current is not None:
        temp = current

        while temp.next is not None:
            if temp.next.value == current.value:
                temp.next = temp.next.next
            else:
                temp = temp.next

        current = current.next

    return head
