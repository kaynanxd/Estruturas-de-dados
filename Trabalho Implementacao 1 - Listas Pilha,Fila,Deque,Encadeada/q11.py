'''Crie um sistema usando uma pilha e uma fila para testar se uma determinada string  ́e um
pal ́ındromo (ou seja, se os caracteres s ̃ao lidos da mesma forma, tanto para a frente quanto
para tr ́as).'''

from q1ArrayStackQueueDeque import ArrayStack, ArrayQueue

def epalindromo(texto):
    pilha = ArrayStack()
    fila = ArrayQueue()

    for caractere in texto:
        pilha.push(caractere)
        fila.enqueue(caractere)

    # Compara removendo um da pilha e um da fila como a pilha renmove de cima e a fila de baixo entao eles devem ser iguais
    while not pilha.is_empty() and not fila.is_empty():
        if pilha.pop() != fila.dequeue():
            return False
    return True


if __name__ == "__main__":
    teste = "radar" 
    if epalindromo(teste):
        print(f'"{teste}" e um palíndromo ')
    else:
        print(f'"{teste}" Nao e um palíndromo ')
