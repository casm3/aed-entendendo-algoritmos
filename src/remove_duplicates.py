from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    anterior = None
    no = head

    while no is not None:
        verificador = head
        ja_visto = False

        while verificador != no:
            if verificador.value == no.value:
                ja_visto = True
                break
            verificador = verificador.next

        if ja_visto:
            anterior.next = no.next  # pula o nó atual
        else:
            anterior = no            # avança o anterior

        no = no.next

    return head