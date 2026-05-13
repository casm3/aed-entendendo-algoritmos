
from src.my_node import MyNode


def reverse_linked_list(head: MyNode) -> MyNode:
    last = None 
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = last
        last = current
        current = next_node
    return last
        