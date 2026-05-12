from src.my_node import MyNode

def reverse_linked_list(head: MyNode) -> MyNode:
    anterior = None
    cabeca = head

    while cabeca: 
        proximo_no = cabeca.next
        cabeca.next = anterior
        anterior = cabeca
        cabeca = proximo_no

    return anterior