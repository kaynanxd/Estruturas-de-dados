"""(Mais um) Vocˆe recebe um inteiro grande representado como um vetor de d ́ıgitos inteiros,

onde cada digitos[i]  ́e o i- ́esimo d ́ıgito do inteiro. Os d ́ıgitos s ̃ao ordenados do mais signi-
ficativo para o menos significativo, da esquerda para a direita. O inteiro grande n ̃ao cont ́em

nenhum 0 `a esquerda. Incremente o inteiro grande em um e retorne o vetor de d ́ıgitos resul-
tante."""

def maisum(lista):
    n = len(lista)
    for i in range (n-1,-1,-1):
        if lista[i]<9:
            lista[i]+=1
            return lista
        lista[i]=0
    return [1] + lista
#basicamente o loop comeca no ultimo indice da lista, ele testa se o ultimo elemento e menor que 9, se sim soma 1 e retorna, se for igual a 9 entao ele coloca um 0 no lugar e prossegue o loop,se todos forem 9 ele zera tudo e retorna com 1 concatenado a esquerda
#complexidade O(n)

print(maisum([1,2,3]))      
print(maisum([4,3,2,1]))   
print(maisum([9]))            