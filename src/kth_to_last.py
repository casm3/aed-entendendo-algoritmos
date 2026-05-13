from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    
    if k <=0:
        return -1
    
    esq = head
    dir = head
    
    
    for i in range (k):
        if dir is None:
            return -1
        dir = dir.next
    while dir is not None:
        dir = dir.next
        esq = esq.next
                
    return esq.value            