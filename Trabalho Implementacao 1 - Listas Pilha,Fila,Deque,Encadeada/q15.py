'''Descreva um algoritmo recursivo que conta o n ́umero de n ́os em uma lista encadeada simples.'''
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def conta_nos(no):
    if no is None: 
        return 0
    return 1 + conta_nos(no.proximo) 

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n1.proximo = n2
    n2.proximo = n3

    print(conta_nos(n1))
