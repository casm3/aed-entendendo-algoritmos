from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    from src.my_node import MyNode

def has_cycle(head: MyNode) -> bool:
    if head is None or head.next is None:
        return False
    
    tartaruga = head
    lebre = head
    
    while lebre is not None and lebre.next is not None:
        tartaruga = tartaruga.next
        lebre = lebre.next.next
        
        if tartaruga == lebre:
            return True
            
    return False