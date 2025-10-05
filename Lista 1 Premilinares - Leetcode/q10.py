"""Exerc ́ıcio: 10.
(Ordenar Vetor por Paridade) Dado um vetor de inteiros nums, mova todos os inteiros
pares no in ́ıcio do vetor, seguidos por todos os inteiros  ́ımpares. Retorne qualquer array que
satisfa ̧ca esta condi ̧c ̃ao.
Exemplo 1. Entrada: nums = [3, 1, 2, 4]. Sa ́ıda: [2,4,3,1]. Explica ̧c ̃ao: As sa ́ıdas
[4,2,3,1], [2,4,1,3] e [4,2,1,3] tamb ́em seriam aceitas.
Exemplo 2. Entrada: nums = [0]. Sa ́ıda: [0]."""

def ordenarparidade(lista):
    pares = []
    impares = []

    for n in lista:
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
    return pares + impares

#cria 2 listas vazias e varre a lista para adicionar os elementos pares e impares respectivos e por ultimo retorna a concatenacao dos dois 
#complexidade O(n)

print(ordenarparidade([3, 1, 2, 4])) 
print(ordenarparidade([0]))           