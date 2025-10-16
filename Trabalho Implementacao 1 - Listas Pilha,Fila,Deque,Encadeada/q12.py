'''Implemente as classes LinkedStack, LinkedQueue, CircularQueue e LinkedDeque.'''
class Node:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo

class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, valor):
        novono = Node(valor, self.top)
        self.top = novono
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Pilha Vazia")
        valor = self.top.valor
        self.top = self.top.proximo
        self.size -= 1
        return valor

    def peek(self):
        if self.is_empty():
            raise Exception("Pilha Vazia")
        return self.top.valor

    def __len__(self):
        return self.size
    
class LinkedQueue:
    def __init__(self):
        self.frente = None
        self.tras = None
        self.size = 0

    def is_empty(self):
        return self.frente is None

    def enqueue(self, valor):
        novono = Node(valor)
        if self.is_empty():
            self.frente = novono
        else:
            self.tras.proximo = novono
        self.tras = novono
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("FIla vazia")
        valor = self.frente.valor
        self.frente = self.frente.proximo
        self.size -= 1
        if self.is_empty():
            self.tras = None
        return valor

    def first(self):
        if self.is_empty():
            raise Exception("FIla vazia")
        return self.frente.valor

    def __len__(self):
        return self.size

class CircularQueue:
    def __init__(self, capacidade):
        self.valor = [None] * capacidade
        self.frente = 0
        self.size = 0
        self.capacidade = capacidade

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacidade

    def enqueue(self, valor):
        if self.is_full():
            raise Exception("fila circular vazia")
        auxiliar = (self.frente + self.size) % self.capacidade
        self.valor[auxiliar] = valor
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("fila circular vazia")
        valor = self.valor[self.frente]
        self.valor[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidade
        self.size -= 1
        return valor

    def first(self):
        if self.is_empty():
            raise Exception("fila circular vazia")
        return self.valor[self.frente]

    def __len__(self):
        return self.size


class DoubleNode:
    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

class LinkedDeque:
    def __init__(self):
        self.frente = None
        self.tras = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, valor):
        novono = DoubleNode(valor, None, self.frente)
        if self.is_empty():
            self.tras = novono
        else:
            self.frente.anterior = novono
        self.frente = novono
        self.size += 1

    def add_last(self, valor):
        novono = DoubleNode(valor, self.tras, None)
        if self.is_empty():
            self.frente = novono
        else:
            self.tras.proximo = novono
        self.tras = novono
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("Deque ta vazia")
        valor = self.frente.valor
        self.frente = self.frente.proximo
        if self.frente is None:
            self.tras = None
        else:
            self.frente.anterior = None
        self.size -= 1
        return valor

    def delete_last(self):
        if self.is_empty():
            raise Exception("Deque ta vazia")
        valor = self.tras.valor
        self.tras = self.tras.anterior
        if self.tras is None:
            self.frente = None
        else:
            self.tras.proximo = None
        self.size -= 1
        return valor

    def first(self):
        if self.is_empty():
            raise Exception("Deque ta vazia")
        return self.frente.valor

    def last(self):
        if self.is_empty():
            raise Exception("Deque ta vazia")
        return self.tras.valor

    def __len__(self):
        return self.size
