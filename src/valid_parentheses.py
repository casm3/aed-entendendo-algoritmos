from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    pilhas = MyStack()
    pares = {')': '(', '}': '{', ']': '['}

    for caractere in string:
        if caractere in "({[":
            pilhas.push(caractere)
        elif caractere in ")}]":
            if pilhas.is_empty():
                return False
            topo = pilhas.pop()
            if pares[caractere] != topo:
                return False
    return pilhas.is_empty()
