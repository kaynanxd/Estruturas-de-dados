from q1ArrayStackQueueDeque import ArrayStack

def inverter_lista(lista):
    pilha = ArrayStack()

    for elem in lista:
        pilha.push(elem)
        
    lista.clear()

    while not pilha.is_empty():
        lista.append(pilha.pop())
        
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    print("Antes:", lista)

    inverter_lista(lista)
    print("Depois:", lista)

