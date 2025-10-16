'''Uma lista encadeada cont ́em alguns n ́umeros positivos e alguns n ́umeros negativos. Usando
essa lista encadeada, escreva um programa para criar duas novas listas encadeadas, uma
contendo todos os n ́umeros positivos e a outra contendo todos os n ́umeros negativos.'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def separar_positivos_negativos(head):
    positivo_head = positivo_cauda = None
    negativo_head = negativo_cauda = None

    atual = head
    while atual:
        novo_no = Node(atual.valor)
        if atual.valor >= 0:
            if positivo_head is None:
                positivo_head = positivo_cauda = novo_no
            else:
                positivo_cauda.proximo = novo_no
                positivo_cauda = novo_no
        else:
            if negativo_head is None:
                negativo_head = negativo_cauda = novo_no
            else:
                negativo_cauda.proximo = novo_no
                negativo_cauda = novo_no
        atual = atual.proximo

    return positivo_head, negativo_head

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(-5)
    n3 = Node(7)
    n4 = Node(-3)
    n5 = Node(2)
    n1.proximo = n2
    n2.proximo = n3
    n3.proximo = n4
    n4.proximo = n5

    positivos, negativos = separar_positivos_negativos(n1)


    def imprimir_lista(head):
        atual = head
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

    print("Positivos:")
    imprimir_lista(positivos)

    print("Negativos:")
    imprimir_lista(negativos)
