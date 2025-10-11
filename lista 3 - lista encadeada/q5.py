'''Exerc ́ıcio: 5.
(Lista Encadeada Inversamente) Dado o cabe ̧calho de uma lista encadeada simples,
inverta a lista e retorne a lista invertida.
Exemplo 1. Entrada: head = [1, 2, 3, 4, 5]. Sa ́ıda: [5,4,3,2,1]
Exemplo 2. Entrada: head = []. Sa ́ıda: [].'''

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

def inverterlista(head):
    anterior = None
    atual=head

    while atual:
        proximo=atual.proximo
        atual.proximo=anterior
        anterior=atual
        atual=proximo
    return anterior

lista = criarlista([1, 2, 3, 4, 5])
print("Lista original:")
imprimirlista(lista)

invertida = inverterlista(lista)
print("Lista invertida:")
imprimirlista(invertida)
