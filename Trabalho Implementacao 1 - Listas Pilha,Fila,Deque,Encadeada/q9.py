from q1ArrayStackQueueDeque import ArrayStack


def prefixa_infixa_e_posfixa(expressao_prefixa):
    pilha_infixa = ArrayStack()
    pilha_posfixa = ArrayStack()

    # Divide a expressão em partes (assumindo que estão separadas por espaços)
    tokens = expressao_prefixa.split()

    # Percorre da direita para a esquerda
    for token in reversed(tokens):
        if token.isdigit():  # se for número
            pilha_infixa.push(token)
            pilha_posfixa.push(token)
        else:  # se for operador
            # Para infixa: adiciona parênteses
            op1 = pilha_infixa.pop()
            op2 = pilha_infixa.pop()
            expressao_infixa = f"({op1} {token} {op2})"
            pilha_infixa.push(expressao_infixa)

            # Para pos fixa
            op1_pos = pilha_posfixa.pop()
            op2_pos = pilha_posfixa.pop()
            expressao_posfixa = f"{op1_pos} {op2_pos} {token}"
            pilha_posfixa.push(expressao_posfixa)

    return pilha_infixa.pop(), pilha_posfixa.pop()


# Exemplo de uso
expressao_prefixa = "* + 2 3 4"
infixa, posfixa = prefixa_infixa_e_posfixa(expressao_prefixa)

print("Prefixa:  ", expressao_prefixa)
print("Infixa:   ", infixa)
print("Pós-fixada:", posfixa)
