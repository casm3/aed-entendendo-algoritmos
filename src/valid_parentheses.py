from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
       stack = MyStack()
       par = {")": "(",
              "]": "[",
              "}": "{"}
       
       for char in string:
           if char in "([{":
               stack.push(char)

           elif char in ")]}":
                if stack.is_empy():
                    return False
                
                remover = stack.pop()
                if remover != par[char]:
                    return False
        
       return stack.is_empyt()