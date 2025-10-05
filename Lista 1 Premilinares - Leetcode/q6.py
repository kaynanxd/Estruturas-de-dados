"""(Mover Zeros) Dado um vetor de inteiros nums, mova todos os 0s para o final dele, man-
tendo a ordem relativa dos elementos diferentes de zero. Observe que vocˆe deve fazer isso no

local, sem fazer uma c ́opia do vetor.
Exemplo 1. Entrada: nums = [0, 1, 0, 3, 12]. Sa ́ıda: [1,3,12,0,0].
Exemplo 2. Entrada: nums = [0]. Sa ́ıda: [0]."""

def moverzeros(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]==0 :
                temp=lista[j]
                lista[j]=lista[i]
                lista[i]=temp
    return lista

#complexidade O(n^2)

print(moverzeros([0,1,0,3,12]))
print(moverzeros([0]))


#versao com complexidade O(n)
def moverzerosv2(lista):
    pos=0
    for i in range(len(lista)):
        if lista[i]!=0:
            lista[pos]=lista[i]
            pos+=1
    for i in range(pos,len(lista)): # coloca os 0 de volta no final
        lista[i]=0
    return lista

#move todos os elementos diferentes de 0 para o inicio da lista e armazena o indice em pos, e por fim um for para colocar os 0 de volta ficando entao O(n)+O(n) = 2O(n), tirando a cosntante somente O(n)

