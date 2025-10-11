'''Exerc ́ıcio: 1.
(Mesclar Suas Listas Ordenadas) Vocˆe recebe os cabe ̧calhos de duas listas encadeadas
ordenadas, lista1 e lista2. Mescle as duas listas em uma lista ordenada. A lista deve ser
formada juntando os n ́os das duas primeiras listas. Retorne o cabe ̧calho da lista encadeada
mesclada.'''

# Definição do nó da lista encadeada, basicamente ele possue 2 atributos, o valor e um campo apontando para o proximo no da lista, ou none se for o ultimo elemento
class node:
    def __init__(self,valor):  # um nó da lista encadeada, def init e um construtor parecido com java
        self.valor=valor
        self.proximo=None #ponteiro referencia para o proximo no da lista, aqui vai ta como none pq vamos considerar q esse e o ultimo elemento da lista

def criarlista(valores): #def para criarmos uma lista encadeada a partir de um vetor contendo valores
    if not valores:
        return None #se a lista nao tiver nada retorna vazio
    
    head = node(valores[0]) #criado o primeiro valor da lista, esse valor vai ser nosso head que e o inicio da lista
    atual = head #aq criamos uma variavel auxiliar pois precisamos guardar o valor do nosso head(inicio da lista), iremos ir incrementando os nos usando a variavel atual

    for valor in valores[1:]: #aqui iteramos o resto dos valores da lista
        atual.proximo = node(valor) #cria um novo no e liga o proximo do no atual a ele
        atual = atual.proximo #move atual para o no seguinte
    return head #retorna a referencia para o no inicial da lista


def imprimirlista(head): #funcao para imprimir a lista
    atual = head #comecamos no primeiro no
    while atual: #enquanto atual nao for none, ou seja ainda houver nos, executa:
        print(atual.valor, end = '->')
        atual=atual.proximo #avanca para o proximo no loop
    print('none')

def mesclarlistas(lista1,lista2): #ela vai receber o head das duas listas
    dummy=node(0) #no ficticio pra facilitar a construcao da lista , vai atuar como o head
    atual=dummy

    while lista1 and lista2: #enquanto umas das duas listas nao acabarem
        if lista1.valor<=lista2.valor: #escolhe o menor valor para ficar em ordem crescente
            atual.proximo = lista1 #liga o no atual da lista1 na lista resultado
            lista1 = lista1.proximo #avanca o no da lista1
        else:
            atual.proximo=lista2 #liga o no atual da lista2 na do resultado
            lista2 = lista2.proximo #avanca o no da lista 2

        atual=atual.proximo #avanca o ponteiro atual para o fim da nova lista

    if lista1: #apos sair do loop uma das listas ainda pode ter elementos sobrando
        atual.proximo=lista1
    else:
        atual.proximo=lista2

    return dummy.proximo #retornamos dummy.proximo que sera o inicio da lista

#complexidade ficou O(n+m)

# Exemplos de teste
lista1 = criarlista([1, 2, 4])
lista2 = criarlista([1, 3, 4])
merged = mesclarlistas(lista1, lista2)
print(imprimirlista(merged))  # Saída: [1, 1, 2, 3, 4, 4]

lista1 = criarlista([])
lista2 = criarlista([])
merged = mesclarlistas(lista1, lista2)
print(imprimirlista(merged))  # Saída: []

