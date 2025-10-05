def numerounico(lista):
    for i in range(len(lista)):  #O(N)
        jaapareceu = 0
        for j in range(len(lista)):  #O(N)
            if i != j and lista[i] == lista[j]:  # compara os elementos menos com a comparacao com ele mesmo
                jaapareceu += 1
        if jaapareceu == 0: 
            return lista[i]

#complexidade O(n^2) por conta dos 2 for que varrem a lista

# Testes
print(numerounico([2, 2, 1]))          # 1
print(numerounico([4, 1, 2, 1, 2]))    # 4
print(numerounico([1]))                # 1

#forma mais eficiente com complexida o(n)
def numerounicov2(lista):
    contagem = {} #dict para armazenar a contagem
    for num in lista:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1

    for num in contagem:
        if contagem[num] == 1:
            return num
        

