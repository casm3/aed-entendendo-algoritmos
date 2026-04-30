from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    if string is None:
        return False
    pilha = MyStack()

    for char in string:
        if char == '(' or char == '[' or char == '{':
            pilha.push(char)
        else:
            if pilha.is_empty():
                return False

            topo = pilha.pop()

            if char == ')' and topo != '(':
                return False
            if char == ']' and topo != '[':
                return False
            if char == '}' and topo != '{':
                return False

    return pilha.is_empty()
