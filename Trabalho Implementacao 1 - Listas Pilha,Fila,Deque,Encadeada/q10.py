from q1ArrayStackQueueDeque import ArrayStack
from q9 import prefixa_infixa_e_posfixa

def calculadora(expressao_posfixa):
    pilha = ArrayStack() 
    
    for token in expressao_posfixa.split():  # <-- transforma string em lista de tokens
        if token.isdigit():  # se for numero
            pilha.push(int(token))
        else:  # operador
            b = pilha.pop()
            a = pilha.pop()
            if token == '+':
                pilha.push(a + b)
            elif token == '-':
                pilha.push(a - b)
            elif token == '*':
                pilha.push(a * b)
            elif token == '/':
                pilha.push(a // b)  # divisão inteira
    return pilha.pop()

if __name__ == "__main__":
    expressao_prefixa = "* + 4 5 6" 
    infixa, posfixa = prefixa_infixa_e_posfixa(expressao_prefixa)

    resultado = calculadora(posfixa)

    print("Prefixa:  ", expressao_prefixa)
    print("Pós-fixada:", posfixa)
    print("Resultado:", resultado)

