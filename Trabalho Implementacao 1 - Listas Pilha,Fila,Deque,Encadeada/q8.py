from q1ArrayStackQueueDeque import ArrayStack

def verificar_parenteses(expressao):
    pilha = ArrayStack()

    for char in expressao:
        if char == '(':
            pilha.push(char)
        elif char == ')':
            if pilha.is_empty():
                return False
            pilha.pop()

    return pilha.is_empty() 

if __name__ == "__main__":
    exp1 = "(1 + 2) * (3 + 4)"
    exp2 = "((1 + 2) * (3 + 4)"

    print(f"Expressão: {exp1}  Bem formada : {verificar_parenteses(exp1)}")
    print(f"Expressão: {exp2}  Bem formada : {verificar_parenteses(exp2)}")