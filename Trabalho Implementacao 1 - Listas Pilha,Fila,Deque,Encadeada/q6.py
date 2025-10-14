from q1ArrayStackQueueDeque import ArrayQueue

fila = ArrayQueue()

fila.enqueue(5)

fila.enqueue(3)

fila.dequeue()

fila.enqueue(2)

fila.enqueue(8)

fila.dequeue()

fila.dequeue()

fila.enqueue(9)

fila.enqueue(1)

fila.dequeue()

fila.enqueue(7)

fila.enqueue(6)

fila.dequeue()

fila.dequeue()

fila.enqueue(4)

fila.dequeue()

fila.dequeue()
print("resultado", fila._data)