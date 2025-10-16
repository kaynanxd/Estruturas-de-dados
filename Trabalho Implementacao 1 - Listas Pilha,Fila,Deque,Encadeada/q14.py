'''Descreva um bom algoritmo para concatenar duas listas encadeadas simples L e M, dadas
apenas referˆencias ao primeiro n ́o de cada lista, em uma  ́unica lista L que cont ́em todos os
n ́os de L seguidos por todos os n ́os de M.'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def concatena(L, M):
    if L is None:
        return M
    atual = L
    while atual.proximo is not None:
        atual = atual.proximo
    atual.proximo = M
    return L


if __name__ == "__main__":
    L = Node(1)
    L.proximo = Node(2)
    L.proximo.proximo = Node(3)

    M = Node(4)
    M.proximo = Node(5)

    R = concatena(L, M)

    atual = R
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.proximo
    print("None")
