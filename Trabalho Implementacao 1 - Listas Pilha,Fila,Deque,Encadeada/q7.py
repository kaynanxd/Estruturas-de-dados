'''Execute a seguinte s ́erie de opera ̧c ̃oes de deque, assumindo uma deque inicialmente vazia:
add first(4), add last(8), add last(9), add first(5), back(), delete first( ), delete last( ), add
last(7), first( ), last( ), add last(6), delete first( ), delete first( ).'''

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