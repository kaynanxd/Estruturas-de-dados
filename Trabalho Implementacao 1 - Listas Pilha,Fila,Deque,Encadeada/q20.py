'''Modifique a classe DoublyLinkedBase para incluir um m ́etodo reverse que inverte a ordem
da lista, mas sem criar ou destruir nenhum n ́o.'''
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class DoublyLinkedBase:
    def __init__(self):
        self.head = None
        self.cauda = None

    def append(self, valor):
        novo_no = Node(valor)
        if self.head is None:
            self.head = self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            novo_no.anterior = self.cauda
            self.cauda = novo_no

    def imprimir(self):
        atual = self.head
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

    def reverse(self):
        atual = self.head
        while atual:

            atual.proximo, atual.anterior = atual.anterior, atual.proximo
            atual = atual.anterior

        self.head, self.cauda = self.cauda, self.head

if __name__ == "__main__":
    lista = DoublyLinkedBase()
    for valor in [10, 20, 30, 40]:
        lista.append(valor)

    print("Lista original:")
    lista.imprimir()

    lista.reverse()
    print("Lista invertida:")
    lista.imprimir()

