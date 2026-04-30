from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if head is None or head.next is None:
        return False

    avanca_um = head
    avanca_dois = head

    while avanca_dois is not None and avanca_dois.next is not None:
        avanca_um = avanca_um.next
        avanca_dois = avanca_dois.next.next

        if avanca_um == avanca_dois:
            return True

    return False
