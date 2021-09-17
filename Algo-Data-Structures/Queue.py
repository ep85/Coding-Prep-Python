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


#examples
#Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
def produce_binary_numbers(n):
    numbers_queue = deque()
    numbers_queue.appendleft("1")

    for i in range(n):
        front = numbers_queue[-1]
        print("   ", front)
        numbers_queue.appendleft(front + "0")
        numbers_queue.appendleft(front + "1")

        numbers_queue.pop()


produce_binary_numbers(10)
