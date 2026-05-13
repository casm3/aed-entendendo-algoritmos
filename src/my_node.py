class MyNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    def __repr__(self) -> str:
        return f"MyNode({self.value})"