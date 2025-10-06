'''(Tempo Necess ́ario para Comprar Ingressos) H ́a n pessoas em uma fila para comprar
ingressos, onde a primeira pessoa est ́a na frente da fila e a n- ́esima pessoa est ́a no final da fila.
Vocˆe recebe um vetor de inteiros tickets de comprimento n, onde o n ́umero de ingressos que
a i- ́esima pessoa gostaria de comprar  ́e tickets[i]. Cada pessoa leva exatamente 1 segundo
para comprar um ingresso. Uma pessoa s ́o pode comprar 1 ingresso por vez e precisa voltar
ao final da fila (o que acontece instantaneamente) para comprar mais ingressos. Se uma
pessoa n ̃ao tiver mais ingressos para comprar, ela sair ́a da fila. Retorne o tempo que a pessoa
inicialmente na posi ̧c ̃ao k levou para finalizar a compra dos ingressos.
Exemplo 1. Entrada: tickets = [2, 3, 2], k = 3. Sa ́ıda: 6. Explica ̧c ̃ao:
A fila come ̧ca como [2, 3, 2], onde a k- ́esima pessoa est ́a sublinhada.
Ap ́os a pessoa da frente comprar um ingresso, a fila se torna [3, 2, 1] em 1 segundo.
Continuando esse processo, a fila se torna [2, 1, 2] em 2 segundos.
Continuando esse processo, a fila se torna [1, 2, 1] em 3 segundos.
Continuando esse processo, a fila se torna [2, 1] em 4 segundos. Observa ̧c ̃ao: a
pessoa da frente saiu da fila.
Continuando esse processo, a fila se torna [1, 1] em 5 segundos.
Continuando esse processo, a fila se torna [1] em 6 segundos. A k- ́esima pessoa
comprou todos os seus ingressos, ent ̃ao retorne 6.
Exemplo 2. Entrada: tickets = [5, 1, 1, 1], k = 1. Sa ́ıda: 8.'''

def temponecessario(tickets,k):
    fila = [(t, i) for i, t in enumerate(tickets)] #armazenamos em fila o valor dos ingressos e o indice
    tempo = 0

    while fila: #enquanto a fila existir iremos remover o primeiro elemento e subtrair 1 ingresso e somar 1 ao tempo
        ingressos, pos = fila.pop(0)
        ingressos-=1
        tempo+=1

        if ingressos>0: # se a pessoa ainda tiver ingressos entao ela ira para o final da fila, quando e feito o append ela e jogada no fim da fila
            fila.append((ingressos,pos))
        elif pos == k: #quando o loop chega na posicao do alvo entao retorna o tempo
            return tempo

#complexidade O(n)
        
print(temponecessario([2, 3, 2], 2))    
print(temponecessario([5, 1, 1, 1], 0)) 
