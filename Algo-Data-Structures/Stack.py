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


# examples

# Reverse a string
from collections import deque
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    #Using a stack for fun
    stack = deque()
    for letter in s:
        stack.append(letter)
        
    arr = []
    while len(stack) != 0:
        charact = stack.pop()
        arr.append(charact)
    
    return arr

reverseString("hello")

# Reverse a string

#Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

def isValid(self, s: str) -> bool:
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = deque()
        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                stack.append(ch)
            if ch ==')' or ch=='}' or ch == ']':
                 if len(stack) == 0:
                        return False
                 if not match_dict[ch] == stack.pop():
                    return False
                
        return len(stack)==0

print(isValid("()"))
print(isValid("({})"))
print(isValid("({{})"))