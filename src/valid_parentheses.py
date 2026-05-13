from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    test_stack = MyStack()
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char in mapping:
            if test_stack.is_empty():
                return False

            top = test_stack.pop()

            if mapping[char] != top:
                return False
        else:
            test_stack.push(char)

    return test_stack.is_empty()