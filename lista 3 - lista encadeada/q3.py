'''(Ciclo de Lista Encadeada) Dado head, o in ́ıcio de uma lista encadeada, determine se
a lista encadeada possui um ciclo. H ́a um ciclo em uma lista encadeada se houver algum
n ́o na lista que possa ser alcan ̧cado novamente seguindo continuamente o pr ́oximo ponteiro.
Internamente, pos  ́e usado para denotar o  ́ındice do n ́o ao qual o pr ́oximo ponteiro est ́a
conectado. Observe que pos n ̃ao  ́e passado como parˆametro.
Retorna verdadeiro se houver um ciclo na lista encadeada. Caso contr ́ario, retorna falso.
Exemplo 1. Entrada: head = [3, 2, 0, −4], pos = 2. Sa ́ıda: verdadeiro. Explica ̧c ̃ao:
H ́a um ciclo na lista encadeada, onde a cauda se conecta ao seguindo n ́o.
Exemplo 2. Entrada: head = [1, 2], pos = 1. Sa ́ıda: verdadeiro. Explica ̧c ̃ao: H ́a
um ciclo na lista encadeada, onde a cauda se conecta ao n ́o 1.
Exemplo 3. Entrada: head = [1], pos = 0. Sa ́ıda: falso. Explica ̧c ̃ao: N ̃ao h ́a ciclo
na lista encadeada.'''

class node:
    def __init__(self,valor):
        self.valor=valor
        self.proximo=None

def criarlista(valores):
    if not valores:
        return None
    
    head=node(valores[0])
    atual=head

    for valor in valores[1:]:
        atual.proximo=node(valor)
        atual = atual.proximo
    return head

def imprimirlista(head):
    atual=head
    while atual:
        print(atual.valor,end='->')
        atual=atual.proximo
    print('none')

#resposta

def temciclo(head):
    visitados=set() #criamos um hashset para armazenar se ja foi visitado ou nao
    atual=head
    while atual:
        if atual in visitados: #se o valor atual ja apareceu no hashsetr entao quer dizer q tem um ciclo
            return True
        visitados.add(atual) #salva o valor no hashset
        atual=atual.proximo
    return False

#complexida O(n)

#teste
n1 = node(3)
n2 = node(2)
n3 = node(0)
n4 = node(-4)

n1.proximo = n2
n2.proximo = n3
n3.proximo = n4
n4.proximo = n2  # cria ciclo conectando com n2

print("Teste 1 (com ciclo):", temciclo(n1))  # esperado: True
