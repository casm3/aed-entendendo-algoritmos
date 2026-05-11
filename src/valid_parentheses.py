# from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:

    pilha = []

    for caractere in string:

        if caractere in "([{":
            pilha.append(caractere)

        else:

            if len(pilha) == 0:
                return False

            topo = pilha.pop()

            if caractere == ")" and topo != "(":
                return False

            if caractere == "]" and topo != "[":
                return False

            if caractere == "}" and topo != "{":
                return False

    return len(pilha) == 0