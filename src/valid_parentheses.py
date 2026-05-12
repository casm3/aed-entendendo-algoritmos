from src.my_stack import MyStack

def is_valid_parentheses(s: str) -> bool:
    pilha = MyStack()   
    pares = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in "({[":
            pilha.push(char)
        elif char in ")}]":
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if topo != pares[char]:
                return False

    return pilha.is_empty()
