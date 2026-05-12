from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in string:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            topo = stack.pop()

            if topo is None or topo != pares[char]:
                return False

    return stack.is_empty()