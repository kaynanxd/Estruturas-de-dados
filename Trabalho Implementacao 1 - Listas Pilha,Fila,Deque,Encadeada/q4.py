from q1ArrayStackQueueDeque import ArrayStack

def limpar_Pilha(S):
    if S.is_empty():
        return
    S.pop()         
    limpar_Pilha(S) 

if __name__ == "__main__":
    S = ArrayStack()
    
    for elem in [1, 2, 3, 4, 5]:
        S.push(elem)
    
    print("Antes de limpar a pilha:", S._data)
    
    limpar_Pilha(S)
    
    print("Depois de limpar a pilha:", S._data)
