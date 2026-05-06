from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()
    for char in string:
        if char in "({[":
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            if char == "}" and top != "{":
                return False
            if char == "]" and top != "[":
                return False
    return stack.is_empty()
