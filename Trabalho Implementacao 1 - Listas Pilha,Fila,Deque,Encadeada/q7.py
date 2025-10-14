from q1ArrayStackQueueDeque import ArrayDeque

dq = ArrayDeque()

dq.add_first(4)

dq.add_last(8)

dq.add_last(9)

dq.add_first(5)

dq.delete_first()

dq.delete_last()

dq.add_last(7)

dq.add_last(6)

dq.delete_first()

dq.delete_first()
print("resultado", dq._data)