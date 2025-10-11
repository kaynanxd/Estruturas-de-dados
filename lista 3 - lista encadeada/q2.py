'''(Remover Duplicatas da Lista Classificada) Dado o cabe ̧calho head de uma lista en-
cadeada ordenada, exclua todas as duplicatas de forma que cada elemento apare ̧ca apenas

uma vez. Retorne a lista encadeada ordenada tamb ́em.
Exemplo 1. Entrada: head = [1, 1, 2]. Sa ́ıda: [1,2].
Exemplo 2. Entrada: head = [1, 1, 2, 3, 3]. Sa ́ıda: [1,2,3].'''

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

#resolucao da questao
def removerduplicatas(head):  #recebemos o head da lista

    atual=head 
    while atual and atual.proximo: #enquanto a lista nao for vazia e o ultimo elmento nao for vazio
        if atual.valor==atual.proximo.valor: #se o valor for igual ao proximo , ele pula um no
            atual.proximo=atual.proximo.proximo
        else:
            atual=atual.proximo #se nao for repetido ele so avanca pro proximo no
    return head

#complexidade O(n)

lista = criarlista([1, 1, 2, 3, 3])
resultado = removerduplicatas(lista)
imprimirlista(resultado)

         


