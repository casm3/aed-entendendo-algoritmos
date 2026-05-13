from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    hare = head
    tortoise = head
    
    if head == None:
        return False
    
    
    
    while hare is not None and hare.next is not None:
    
        hare = hare.next.next 
        
        tortoise = tortoise.next 
        
        if hare == tortoise:
            return True
    return False
        
         