from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    
    pilha = MyStack()  #Começa vazia

    pares = {')': '(',
             '}': '{',
             ']': '['}

    for char in string:
        if char in '({[':
            pilha.push(char) 

        elif char in ')}]':
            if pilha.is_empty():
                return False
            
            topo = pilha.pop()
            
            if  pares[char] != topo:
                return False
            
    return pilha.is_empty()