'''Implemente uma fun ̧c ̃ao com assinatura transfer(S, T) que transfira todos os elementos da
pilha S para a pilha T, de modo que o elemento que come ̧ca no topo de S seja o primeiro a
ser inserido em T, e o elemento na parte inferior de S termine no topo de T.'''

from q1ArrayStackQueueDeque import ArrayStack


def transfer(S, T):

    if S.is_empty():
        return
    
    top_elem = S.pop()
    transfer(S, T)
    T.push(top_elem)


if __name__ == "__main__":
    S = ArrayStack()
    T = ArrayStack()

    for elem in [10, 20, 30, 40, 50]:
        S.push(elem)

    print("Antes da transferência:")
    print("Pilha S:", S._data)
    print("Pilha T:", T._data)

    transfer(S, T)

    print("\nDepois da transferência:")
    print("Pilha S:", S._data)
    print("Pilha T:", T._data)

