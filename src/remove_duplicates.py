from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    
    esq = head
    
    while esq is not None:
        
        dir_old = esq
        dir = esq.next
        
        while dir is not None:
            if dir.value == esq.value:
                dir_old.next = dir.next
                dir = dir.next
            else: 
                dir_old = dir
                dir = dir.next
        
        esq = esq.next               
    
    return head    
#verificar dps 