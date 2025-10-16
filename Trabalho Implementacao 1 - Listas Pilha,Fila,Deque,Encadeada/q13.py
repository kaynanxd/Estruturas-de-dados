'''Forne ̧ca um algoritmo para encontrar o pen ́ultimo n ́o em uma lista encadeada simples na
qual o  ́ultimo n ́o  ́e indicado por uma pr ́oxima referˆencia de None.'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def encontrarpenultimo(head):
    if head is None or head.proximo is None:
        return None 

    atual = head
    while atual.proximo.proximo is not None:
        atual = atual.proximo

    return atual


if __name__ == "__main__":

    head = Node(10)
    head.proximo = Node(20)
    head.proximo.proximo = Node(30)
    head.proximo.proximo.proximo = Node(40)

    penultimo = encontrarpenultimo(head)
    if penultimo:
        print("Penúltimo no e:", penultimo.valor)
    else:
        print("A lista não tem penúltimo no")
