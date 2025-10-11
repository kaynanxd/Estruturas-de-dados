'''Exerc ́ıcio: 10.
(Trocar N ́os em Pares) Dada uma lista encadeada, troque a cada dois n ́os adjacentes e
retorne sua cabe ̧ca. Vocˆe deve resolver o problema sem modificar os valores nos n ́os da lista
(ou seja, apenas os pr ́oprios n ́os podem ser alterados).
Exemplo 1. Entrada: head = [1, 2, 3, 4]. Sa ́ıda: [2,1,4,3].
Exemplo 2. Entrada: head = [1, 2, 3]. Sa ́ıda: [2,1,3].'''

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

def trocarPares(head):
    dummy=node(0)
    dummy.proximo=head
    anterior=dummy

    while anterior.proximo and anterior.proximo.proximo:
        primeiro=anterior.proximo
        segundo=primeiro.proximo

        primeiro.proximo=segundo.proximo
        segundo.proximo=primeiro
        anterior.proximo=segundo

        anterior=primeiro
    return dummy.proximo

lista1 = criarlista([1, 2, 3, 4])
lista2 = criarlista([1, 2, 3])

print("Lista original 1:")
imprimirlista(lista1)
print("Depois da troca:")
imprimirlista(trocarPares(lista1))

print("\nLista original 2:")
imprimirlista(lista2)
print("Depois da troca:")
imprimirlista(trocarPares(lista2))
