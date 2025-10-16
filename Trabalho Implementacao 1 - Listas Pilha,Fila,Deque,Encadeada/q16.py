'''Implemente uma fun ̧c ̃ao que conta o n ́umero de n ́os em uma lista circularmente encadeada.'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None  

def contar_nos_circular(head):
    if head is None:
        return 0

    count = 1
    atual = head.proximo

    while atual != head:
        count += 1
        atual = atual.proximo

    return count



if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)

    n1.proximo = n2
    n2.proximo = n3
    n3.proximo = n1 
    print(contar_nos_circular(n1))
