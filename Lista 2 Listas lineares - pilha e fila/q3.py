'''Exerc ́ıcio: 3.
(Pre ̧cos Finais com Desconto Especial em Loja) Vocˆe recebe um vetor de inteiros
precos, onde precos[i]  ́e o pre ̧co do i- ́esimo item em uma loja. H ́a um desconto especial para
itens na loja. Se vocˆe comprar o i- ́esimo item, receber ́a um desconto equivalente a precos[j],
onde j  ́e o  ́ındice m ́ınimo tal que j > i e precos[j] ≤ precos[i]. Caso contr ́ario, vocˆe n ̃ao
receber ́a nenhum desconto. Retorne um vetor de inteiros resposta, onde resposta[i]  ́e o pre ̧co
final que vocˆe pagar ́a pelo i- ́esimo item da loja, considerando o desconto especial.
Exemplo 1. Entrada: precos = [8, 4, 6, 2, 3]. Sa ́ıda: [4,2,4,2,3]. Explica ̧c ̃ao:
Para o item 1 com preco[1] = 8, vocˆe receber ́a um desconto equivalente a
precos[2] = 4; portanto, o pre ̧co final que vocˆe pagar ́a ser ́a 8 − 4 = 4.
Para o item 2 com preco[2] = 4, vocˆe receber ́a um desconto equivalente a
precos[4] = 2; portanto, o pre ̧co final que vocˆe pagar ́a ser ́a 4 − 2 = 2.
Para o item 3 com preco[3] = 6, vocˆe receber ́a um desconto equivalente a
precos[4] = 2; portanto, o pre ̧co final que vocˆe pagar ́a ser ́a 6 − 2 = 4.
Para os itens 3 e 4, vocˆe n ̃ao receber ́a nenhum desconto.
Exemplo 2. Entrada: precos = [1, 2, 3, 4, 5]. Sa ́ıda: [1,2,3,4,5].
Exemplo 3. Entrada: precos = [10, 1, 1, 6]. Sa ́ıda: [9,0,1,6].'''

def precosfinais(lista):
    n = len(lista)
    resposta = lista[:]
    pilha=[]

    for i in range(n):
        while pilha and lista[i]<=lista[pilha[-1]]:
            j = pilha.pop()
            resposta[j]= lista[j]-lista[i]
        pilha.append(i)

    return resposta

#basicamente vamos copiar a lista original e criar uma pilha para guardar o indice da lista de espera
#se a pilha esta vazia entao ja adiciona o indice i inicial a ela nao entrando no while, e comparando os elemetos da lista se o valor for menor ou igual ao indice no final da pilha entra num loop que calcula a resposta , fazendo um pop na pilha e diminuindo i de j
#por exemplo quando a ordem esta [10,1], o 10 passa direto pq e o primeiro elemento, mas quando chega o lista[2]=1, ele compara e ver que 1 e menor que 10, entao remove o 10 da pilha e faz o calculo da resposta e armazena na lista resposta

#complexidade O (n)

print(precosfinais([1,2,3,4,5]))
print(precosfinais([10,1,1,6]))


