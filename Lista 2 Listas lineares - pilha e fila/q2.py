''''Exerc ́ıcio: 2.
(Jogo de Beisebol) Vocˆe est ́a registrando os placares de um jogo de beisebol com regras
estranhas. No in ́ıcio do jogo, vocˆe come ̧ca com um registro vazio.
Vocˆe recebe uma lista de strings ops, onde ops[i]  ́e a i- ́esima opera ̧c ̃ao que vocˆe deve aplicar
ao registro e  ́e uma das seguintes:
 Um inteiro x. Registre uma nova pontua ̧c ̃ao de x.
 ’+’. Registre uma nova pontua ̧c ̃ao que seja a soma das duas pontua ̧c ̃oes anteriores.
 ’D’. Registre uma nova pontua ̧c ̃ao que seja o dobro da pontua ̧c ̃ao anterior.
 ’C’. Invalide a pontua ̧c ̃ao anterior, removendo-a do registro.
Retorne a soma de todas as pontua ̧c ̃oes no registro ap ́os aplicar todas as opera ̧c ̃oes.
Exemplo 1. Entrada: ops = [5, 2, C, D, +]. Sa ́ıda: 30. Explica ̧c ̃ao:
5 - Adicione 5 ao registro, o registro agora  ́e [5].
2 - Adicione 2 ao registro, o registro agora  ́e [5, 2].
C - Invalida e remove a pontua ̧c ̃ao anterior, o registro agora  ́e [5].
D - Adicione 2 * 5 = 10 ao registro, o registro agora  ́e [5, 10].

1

+ - Adicione 5 + 10 = 15 ao registro, o registro agora  ́e [5, 10, 15].
A soma total  ́e 5 + 10 + 15 = 30.'''

#otimo caso para usar a estrutura pilha, iremos varrer a lista e para cada elemento iremos manipular a pilha conforme o enunciado

def jogobaisebol(lista):
    pilha=[]

    for elem in lista:
        if elem == 'C':
            pilha.pop()
        elif elem == 'D':
            pilha.append(2*pilha[-1])
        elif elem == '+':
            pilha.append(pilha[-1]+pilha[-2])
        else:
            pilha.append(elem)
    return sum(pilha)

#complexidade O(N) por conta que varre toda lista, mas as operacoes de insercao e remocao sao O(1) devido a pilha

print(jogobaisebol([5, 2, "C", "D", "+"]))
print(jogobaisebol([5, -2, 4, "C", "D", 9, "+", "+"]))

