'''Exerc ́ıcio: 9.
(Revelar Cartas em Ordem Crescente) Vocˆe recebe um baralho de matrizes de inteiros.
H ́a um baralho de cartas em que cada carta possui um n ́umero inteiro  ́unico. O n ́umero
inteiro na i- ́esima carta  ́e baralho[i]. Vocˆe pode ordenar o baralho na ordem que desejar.
Inicialmente, todas as cartas come ̧cam viradas para baixo (n ̃ao reveladas) em um baralho.
Vocˆe executar ́a os seguintes passos repetidamente at ́e que todas as cartas sejam reveladas:
 Pegue a carta do topo do baralho, revele-a e retire-a do baralho.
 Se ainda houver cartas no baralho, coloque a pr ́oxima carta do topo do baralho no
fundo do baralho.
 Se ainda houver cartas n ̃ao reveladas, volte para a etapa 1. Caso contr ́ario, pare.
Retorne uma ordena ̧c ̃ao do baralho que revelaria as cartas em ordem crescente.
Exemplo 1. Entrada: baralho = [17, 13, 11, 2, 3, 5, 7]. Sa ́ıda: [2,13,3,11,5,17,7].
Explica ̧c ̃ao:

Pegamos o baralho na ordem [17,13,11,2,3,5,7] (essa ordem n ̃ao importa) e o reor-
denamos.

5

Ap ́os a reordena ̧c ̃ao, o baralho come ̧ca como [2,13,3,11,5,17,7], onde 2  ́e o topo do
baralho.
Revelamos 2 e movemos 13 para o fundo. O baralho agora  ́e [3,11,5,17,7,13].
Revelamos 3 e movemos 11 para o fundo. O baralho agora  ́e [5,17,7,13,11].
Revelamos 5 e movemos 17 para o fundo. O baralho agora  ́e [7,13,11,17].
Revelamos 7 e movemos 13 para o fundo. O baralho agora  ́e [11,17,13].
Revelamos 11 e movemos 17 para o fundo. O baralho agora  ́e [13,17].
Revelamos 13 e movemos 17 para o fundo. O baralho agora  ́e [17].
Revelamos 17.
Como todas as cartas reveladas est ̃ao em ordem crescente, a resposta est ́a correta.'''

def revelarcartas(baralho):
    for i in range(len(baralho)): #coloca em ordem crescente
        for j in range(i+1,len(baralho)):
            if baralho[j]<baralho[i]:
                baralho[i], baralho[j] = baralho[j], baralho[i]
        
    fila=[]

    for i in range(len(baralho)-1 ,-1,-1):
        if len(fila)>0:
            topo = fila.pop()
            fila.insert(0,topo)
        fila.insert(0, baralho[i])

    return fila

baralho = [17, 13, 11, 2, 3, 5, 7]
print(revelarcartas(baralho))
