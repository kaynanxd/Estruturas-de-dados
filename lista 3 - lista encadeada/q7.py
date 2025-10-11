'''Exerc ́ıcio: 7.
(Meio da Lista Encadeada) Dado o cabe ̧calho de uma lista encadeada simples, retorne o
n ́o do meio da lista encadeada. Se houver dois n ́os do meio, retorne o segundo n ́o do meio.
Exemplo 1. Entrada: head = [1, 2, 3, 4, 5]. Sa ́ıda: [3,4,5]. Explica ̧c ̃ao: O n ́o do
meio da lista  ́e o n ́o 3.
Exemplo 2. Entrada: head = [1, 2, 3, 4, 5, 6]. Sa ́ıda: [4,5,6]. Explica ̧c ̃ao: Como a
lista possui dois n ́os do meio com valores 3 e 4, retornamos o segundo.'''

class node:
    def __init__(self,valor):
        self.valor=valor
        self.proximo=None

    
def criarlista(valores):
    if not valores:
        return None
    
    head=node(valores[0])
    atual=head

    for valor in valores[1:]:
        atual.proximo=node(valor)
        atual = atual.proximo
    return head

def imprimirlista(head):
    atual=head
    while atual:
        print(atual.valor,end='->')
        atual=atual.proximo
    print('none')   

def meiodalista(head):
    slow=head
    fast=head

    while fast and fast.proximo:
        slow=slow.proximo
        fast=fast.proximo.proximo

    return slow

lista1 = criarlista([1, 2, 3, 4, 5])
lista2 = criarlista([1, 2, 3, 4, 5, 6])

print("Meio da lista 1:")
imprimirlista(meiodalista(lista1))  # saída esperada: 3->4->5->None

print("Meio da lista 2:")
imprimirlista(meiodalista(lista2))  # saída esperada: 4->5->6->None
