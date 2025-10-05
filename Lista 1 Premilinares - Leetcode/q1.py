"""(Numero Faltante) Dado um vetor nums contendo n n ́umeros distintos no intervalo [0, n],
retorna o  ́unico n ́umero no intervalo que est ́a faltando no array."""

def numerofaltando(lista):
    totalelementos = len(lista) #funcao do python que pega o tamanho do vetor
    soma_esperada = (totalelementos * (totalelementos + 1))/ 2  
    soma_real = sum(lista) #funcao do python para somar tudo que ta no vetor , Obs ela e O(N)
    return soma_esperada - soma_real

#Complexidade O(N)

#como temos todos os numeros da lista de 0 ate n a soma esperada deles 
#pode ser calculada com a formula n * (n+1) / 2 (fórmula da soma dos números inteiros consecutivos)
#caso a nossa lista tenha um numero faltando a soma real dos elementos 
#vai ser menos que a esperada, e a diferenca vai ser o numero faltando

print(numerofaltando([3, 0, 1]))              # deve sair 2
print(numerofaltando([0, 1]))                 # deve sair 2
print(numerofaltando([9,6,4,2,3,5,7,0,1]))    # deve sair 8


