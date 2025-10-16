'''Descreva um algoritmo recursivo r ́apido para reverter uma lista encadeada simples.'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def reverter(head):
    if head is None or head.proximo is None:
        return head
    
    novo_head = reverter(head.proximo)
    head.proximo.proximo = head
    head.proximo = None
    return novo_head

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.proximo = n2
    n2.proximo = n3
    n3.proximo = n4

    head_revertida = reverter(n1)

    atual = head_revertida
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.proximo
    print("None")
