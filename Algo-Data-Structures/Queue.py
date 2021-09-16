'''
Queue

First in first out (FIFO)
Could be used as a stream of data
Stock prices producing and many consumers off this queue

Enqueueing O(1)
Dequeueing O(1)
Searching O(n)

'''
from collections import deque
queue = deque()
queue.appendleft("test1")
queue.appendleft("test2")
queue.appendleft("test3")

queue.pop()
# test1
queue.pop()
# test2
queue.pop()
# test3


