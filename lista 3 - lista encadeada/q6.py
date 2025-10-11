'''Exerc ́ıcio: 6.
(Lista Encadeada de Pal ́ındromos) Dado o cabe ̧calho de uma lista encadeada simples,
retorna verdadeiro se for um pal ́ındromo ou falso caso contr ́ario.
Exemplo 1. Entrada: head = [1, 2, 2, 1]. Sa ́ıda: verdadeiro.
Exemplo 2. Entrada: head = [1, 2]. Sa ́ıda: falso.'''

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

def listaencadeadapalindromo(head):
    valores=[]
    atual=head
    while atual:
        valores.append(atual.valor)
        atual=atual.proximo

    return valores == valores[::-1]

lista1 = criarlista([1, 2, 2, 1])
lista2 = criarlista([1, 2])

print("Teste 1:", listaencadeadapalindromo(lista1))  # True
print("Teste 2:", listaencadeadapalindromo(lista2))  # False
