from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    
    stack = MyStack() 
    
    for i in string:
        
        if stack.is_empty() and i in "}])":
            return False
        
        if i in "{[(":
            stack.push(i)
        
        if i in "}])":
            removed_item = stack.pop()    
            if removed_item + i not in "{}[]()":
                return False
    
    if stack.is_empty():
        return True
    else:
        return False       
        
print(is_valid_parentheses("({}[])"))
   
            
    
        
    
