"""(Interse ̧c ̃ao de Dois Vetores) Dados dois vetores de inteiros, nums1 e nums2, retorne um
vetor de suas interse ̧coes. Cada elemento no resultado deve ser  ́unico e vocˆe pode retornar o
resultado em qualquer ordem."""
''
def doisvetores(nums1,nums2):
    intersecao = [] #vetor para armazenar as intersecoes
    for num in nums1 : #para todo numero que esta no vetor nums1 faca...
        if num in nums2 and num not in intersecao: # o in aqui pecorre cada elemento do vetor 2 para verificar se ele ja existe
            intersecao.append(num) #adiciona o numero no vetor intersecao
    return intersecao

#complexidade O(n)+O(m)

print(doisvetores([1, 2, 2, 1], [2, 2]))  
print(doisvetores([4, 9, 5], [9, 4, 9, 8, 4]))   
