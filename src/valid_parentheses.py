# from src.my_stack import MyStack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None

        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None


def is_valid_parentheses(s):
    stack = Stack()

    for char in s:
        if char in "([{":
            stack.push(char)

        else:
            top = stack.pop()

            if top is None:
                return False

            if char == ")" and top != "(":
                return False

            if char == "]" and top != "[":
                return False

            if char == "}" and top != "{":
                return False

    return stack.is_empty()
