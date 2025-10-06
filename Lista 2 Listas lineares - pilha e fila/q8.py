'''(N ́umero de Alunos que n ̃ao Conseguem Almo ̧car) O refeit ́orio da escola oferece
sandu ́ıches circulares e quadrados no intervalo do almo ̧co, designados pelos n ́umeros 0 e 1,

respectivamente. Todos os alunos formam uma fila. Cada aluno prefere sandu ́ıches quadra-
dos ou circulares. O n ́umero de sandu ́ıches no refeit ́orio  ́e igual ao n ́umero de alunos. Os

sandu ́ıches s ̃ao colocados em uma pilha. Em cada etapa:
 Se o aluno da frente da fila preferir o sandu ́ıche do topo da pilha, ele o pegar ́a e sair ́a
da fila.
 Caso contr ́ario, ele o deixar ́a e ir ́a para o final da fila.

Isso continua at ́e que nenhum dos alunos da fila queira pegar o sandu ́ıche do topo e, por-
tanto, n ̃ao consiga comer. Vocˆe recebe dois vetores de inteiros, alunos e sanduiches, onde

sanduiches[i]  ́e o tipo do i- ́esimo sandu ́ıche na pilha (i = 0  ́e o topo da pilha) e alunos[j]  ́e
a preferˆencia do j- ́esimo aluno na fila inicial (j = 0  ́e o in ́ıcio da fila). Retorne o n ́umero de
alunos que n ̃ao conseguem comer.

4

Exemplo 1. Entrada: alunos = [1, 1, 0, 0], sanduiches = [0, 1, 0, 1]. Sa ́ıda: 0.
Explica ̧c ̃ao:
O aluno da frente sai do sandu ́ıche de cima e retorna ao final da fila, resultando
em alunos = [1,0,0,1].
O aluno da frente sai do sandu ́ıche de cima e retorna ao final da fila, resultando
em alunos = [0,0,1,1].
O aluno da frente pega o sandu ́ıche de cima e sai da fila, resultando em alunos =
[0,1,1] e sandu ́ıches = [1,0,1].
O aluno da frente sai do sandu ́ıche de cima e retorna ao final da fila, resultando
em alunos = [1,1,0].
O aluno da frente pega o sandu ́ıche de cima e sai da fila, resultando em alunos =
[1,0] e sandu ́ıches = [0,1].
O aluno da frente sai do sandu ́ıche de cima e retorna ao final da fila, resultando
em alunos = [0,1].
O aluno da frente pega o sandu ́ıche de cima e sai da fila, resultando em alunos =
[1] e sandu ́ıches = [1].
O aluno da frente pega o sandu ́ıche de cima e sai da fila, formando alunos = [] e
sandu ́ıches = [].
Portanto, todos os alunos conseguem comer.
Exemplo'''

def naoconseguemalmocar(alunos,sanduiches):
    fila = alunos[:] #copia a lista dentro da fila
    pilha = sanduiches[:]  #copia a lista dentro da pilha
 
    contador=0 #contador para saber quantos alunos nao comeram

    while fila and contador<len(fila): #roda enquanto tiver alunos na fila, se o contador ficar maior que o tamanho da fila entao quer dizer que ngm vai querer comer mais
        if fila[0]==pilha[0]: #se o aluno comer, remove elemento do inicio
            fila.pop(0) 
            pilha.pop(0)
            contador=0
        else:
            fila.append(fila.pop(0)) #se o aluno nao comer, remove do incio e coloca no fim e soma o contador
            contador+=1
    return len(fila)
        
#complexidade O(n)

print(naoconseguemalmocar([1,1,0,0], [0,1,0,1])) 
print(naoconseguemalmocar([1,1,1,0,0,1], [1,0,0,0,1,1]))  