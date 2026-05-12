from src.my_stack import MyStack


def is_valid_parentheses(s: str) -> bool:
    stack = MyStack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.push(char)
        else:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()
