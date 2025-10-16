'''Escreva um programa para excluir elementos duplicados em uma lista duplamente encadeada.'''
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def remover_duplicatas(head):
    if head is None:
        return None

    valores_vistos = set()
    atual = head

    while atual:
        if atual.valor in valores_vistos:
           
            if atual.proximo:
                atual.proximo.anterior = atual.anterior
            if atual.anterior:
                atual.anterior.proximo = atual.proximo
            else:
                
                head = atual.proximo
        else:
            valores_vistos.add(atual.valor)
        atual = atual.proximo

    return head


if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(10)
    n4 = Node(30)
    n5 = Node(20)

    n1.proximo = n2
    n2.anterior = n1
    n2.proximo = n3
    n3.anterior = n2
    n3.proximo = n4
    n4.anterior = n3
    n4.proximo = n5
    n5.anterior = n4

    head = remover_duplicatas(n1)

    def imprimir_lista(head):
        atual = head
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

    imprimir_lista(head)
