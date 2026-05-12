# from src.my_stack import MyStack


from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    i = 0

    while i < len(string):
        char = string[i]

        if char == "(" or char == "[" or char == "{":
            stack.push(char)

        else:
            if stack.is_empty():
                return False

            top = stack.pop()

            if char == ")" and top != "(":
                return False

            if char == "]" and top != "[":
                return False

            if char == "}" and top != "{":
                return False

        i += 1

    return stack.is_empty()
