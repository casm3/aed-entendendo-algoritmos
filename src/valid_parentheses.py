from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caractere in string:

        # Se for abertura, empilha
        if caractere in "([{":
            stack.push(caractere)

        # Se for fechamento
        elif caractere in ")]}":

            # Se a pilha estiver vazia, inválido
            if stack.is_empty():
                return False

            topo = stack.pop()

            # Verifica se corresponde ao par correto
            if topo != pares[caractere]:
                return False

    # No final, a pilha deve estar vazia
    return stack.is_empty()