'''
(Duas Somas) Dado um vetor de n ́umeros inteiros nums e um alvo inteiro, retorne os
 ́ındices dos dois n ́umeros de forma que a soma deles resulte no alvo. Vocˆe pode assumir que
cada entrada teria exatamente uma solu ̧c ̃ao e n ̃ao pode usar o mesmo elemento duas vezes.
Vocˆe pode retornar a resposta em qualquer ordem.
'''
def duassomas(lista, alvo):
    for contador in range(len(lista)): #O(N)
        for contador2 in range(contador+1, len(lista)): #O(N)
            if lista[contador] + lista[contador2] == alvo:
                return contador, contador2
            
#Resumindo a funcao pecorre a lista e testa todas somas possiveis entre os elementos ate encontrar o alvo
#complexidade O(n^2) por conta dos 2 for que varrem a lista

print(duassomas([2,7,11,15],9))
print(duassomas([3,2,4],6))
print(duassomas([3,3],6))
    