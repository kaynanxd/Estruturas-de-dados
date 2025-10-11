'''Exerc ́ıcio: 4.
(Remover Elementos da Lista Encadeada) Dado o cabe ̧calho de uma lista encadeada e
um inteiro val, remova todos os n ́os da lista encadeada que tenham Node.val = val e retorne
o novo cabe ̧calho.
Exemplo 1. Entrada: head = [1, 2, 6, 3, 4, 5, 6], val = 6. Sa ́ıda: [1,2,3,4,5].
Exemplo 2. Entrada: head = [], val = 1. Sa ́ıda: [].
Exemplo 3. Entrada: head = [7, 7, 7, 7], val = 7. Sa ́ıda: [].'''

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

def removerelemento(head,alvo):
    dummy=node(0)
    dummy.proximo = head
    atual = dummy

    while atual.proximo:
        if atual.proximo.valor == alvo:
            atual.proximo = atual.proximo.proximo
        else:
            atual=atual.proximo
    return dummy.proximo

lista = criarlista([1,2,6,3,4,5,6])
resultado = removerelemento(lista, 6)
imprimirlista(resultado)  # saída esperada: 1->2->3->4->5->none


