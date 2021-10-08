'''

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated 
calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the 
results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization 
reduces time complexities from exponential to polynomial.


1. Recursion
2. Store
3. Bottom up



'''



# Function for nth Fibonacci number
# RECURSIVE
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


# DYNAMIC PROGRAMMING
# Fibonacci Series using Dynamic Programming
def fibonacci(n):
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(9))


'''
Interview Problem

https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can 
be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

'''


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1)
        dp[len(s)] = True
        for i in range(len(s) -1,-1, -1):
            for w in wordDict:
                print("jere", s[i:i+len(w)])
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break 
        print(dp)
        return dp[0]