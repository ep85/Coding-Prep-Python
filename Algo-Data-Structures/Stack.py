'''
Stack

Last in first out (LIFO)

Push/Pop O(1)
Search O(n)

'''

#Example 
from collections import deque
stack = deque()
stack.push("test1")
stack.push("test2")
stack.size()
# 2
stack.peak()
# test2
stack.pop()
# test2
stack.pop()
# test1
