"""(Cont ́em Duplicado) Dado um vetor de inteiros nums, retorna true se qualquer valor
aparecer pelo menos duas vezes no vetor, e retorna false se cada elemento for distinto.
"""

def contemduplicado(lista):
    for contador in range(len(lista)):  #O(N)
        for contador2 in range(contador+1,len(lista)):  #O(N)
            if lista[contador]==lista[contador2]:
                return True
    return False

#complexidade O(n^2) por conta dos 2 for que varrem a lista

print(contemduplicado([1,2,3,1]))
print(contemduplicado([1,2,3,4]))
print(contemduplicado([1,1,1,3,3,4,3,2,4,2]))

#Forma mais eficiente de resolver com complexidade O(N) somente
def contemduplicadov2(lista):
    numerosvistos = {} #dict que funciona parecido com um hashmap, vamos usar apenas para marcar como verdadeiro

    for numero in lista:
        if numero in numerosvistos: 
            return True
        numerosvistos[numero] = True
    return False   