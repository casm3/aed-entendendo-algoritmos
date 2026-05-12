from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    
    esq = head
    
    while esq is not None:
        
        dir = esq
        
        while dir and dir.next is not None:
            dir_old = dir
            dir = dir_old.next
            dir_new = dir.next
            if dir.value == esq.value:
                dir_old.next = dir_new
            dir = dir_old
        
        esq = esq.next               
    
    return head    
#verificar dps 