'''Exerc ́ıcio: 4.
(Pasta de log do rastreador) O sistema de arquivos Leetcode mant ́em um log sempre que
um usu ́ario realiza uma opera ̧c ̃ao de altera ̧c ̃ao de pasta. As opera ̧c ̃oes s ̃ao descritas abaixo:
../: Move para a pasta pai da pasta atual. (Se vocˆe j ́a estiver na pasta principal,
permane ̧ca na mesma pasta).
./: Permanece na mesma pasta.
x/: Move para a pasta filha chamada x (E garantido que esta pasta sempre exista).  ́
Vocˆe recebe uma lista de strings logs, onde logs[i]  ́e a opera ̧c ̃ao realizada pelo usu ́ario na
etapa i. O sistema de arquivos inicia na pasta principal e, em seguida, as opera ̧c ̃oes em logs
s ̃ao realizadas. Retorne o n ́umero m ́ınimo de opera ̧c ̃oes necess ́arias para retornar `a pasta
principal ap ́os as opera ̧c ̃oes de altera ̧c ̃ao de pasta.
Exemplo 1. Entrada: logs = [d1/, d2/, ../, d21/, ./]. Sa ́ıda: 2. Explica ̧c ̃ao: Use
esta opera ̧c ̃ao de altera ̧c ̃ao de pasta ../ 2 vezes e retorne `a pasta principal.
Exemplo 2. Entrada: logs = [d1/, d2/, ./, d3/, ../, d31/]. Sa ́ıda: 3.
Exemplo 3. Entrada: logs = [d1/, ../, ../, ../]. Sa ́ıda: 0.'''

def pastalog(lista):
    n = len(lista)
    pilha = []

    for elem in lista:
        if elem=='../': #remove 1 elemento, caso esteja vazia nao faz nada
            if not pilha:
                break
            pilha.pop()
        elif elem=='./': #apenas prossegue
            continue
        else: #caso a variavel seja x/ entao vai adicionar esse elemento na pilha
            pilha.append(elem)
    return len(pilha)

#complexidade o de n
#resolucao parecida com a q2, basicamente criamos uma pilha e armazenamos os elementos nela, aplicando as condicoes de entrada, e por fim devolvendo a quantidade de elementos que sobraram apos as operacoes

print(pastalog(['d1/', 'd2/', './', 'd3/', '../', 'd31/']))
print(pastalog(['d1/', '../', '../', '../']))


