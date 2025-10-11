'''Exerc ́ıcio: 9.
(Adicione Dois N ́umeros) Vocˆe recebe duas listas encadeadas n ̃ao vazias representando
dois n ́umeros inteiros n ̃ao negativos. Os d ́ıgitos s ̃ao armazenados em ordem inversa e cada um
de seus n ́os cont ́em um  ́unico d ́ıgito. Some os dois n ́umeros e retorne a soma como uma lista
encadeada. Vocˆe pode assumir que os dois n ́umeros n ̃ao contˆem nenhum zero `a esquerda,
exceto o pr ́oprio n ́umero 0.
Exemplo 1. Entrada: L1 = [2, 4, 3], L2 = [5, 6, 4]. Sa ́ıda: [7,0,8]. Explica ̧c ̃ao: 342
+ 465 = 807.
Exemplo 2. Entrada: L1 = [9, 9, 9, 9, 9, 9, 9], L2 = [9, 9, 9, 9]. Sa ́ıda: [8,9,9,9,0,0,0,1].'''

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
def somarListas(lista1,lista2):
    dummy=node(0)
    atual=dummy
    carry=0

    while lista1 or lista2 or carry:
        valor1=lista1.valor if lista1 else 0 #Se lista1 ainda tem nó pega o valor do nó se lista 1 acabou considera 0
        valor2=lista2.valor if lista2 else 0

        total= valor1+valor2 + carry
        carry= total // 10
        atual.proximo = node(total%10)
        atual= atual.proximo

        if lista1:
            lista1=lista1.proximo
        if lista2:
            lista2=lista2.proximo
    return dummy.proximo

L1 = criarlista([2,4,3])
L2 = criarlista([5,6,4])
resultado = somarListas(L1, L2)
imprimirlista(resultado)  

L3 = criarlista([9,9,9,9,9,9,9])
L4 = criarlista([9,9,9,9])
resultado2 = somarListas(L3, L4)
imprimirlista(resultado2) 
