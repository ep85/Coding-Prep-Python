'''
Arrays

In python these are dynamic arrays, size can grow, dimensional arrays

Initialize
stock_prices = []

Retrieve O(1)
 stock_prices[0]
Insert O(1)
 stock_prices.insert(1, 292) or append for adding to backDelete O(1) 
 stock_prices.remove(1)
Delete O(1) 
 stock_prices.remove(1)

LeetCodes
https://leetcode.com/tag/array/

Exercise 
-Let us say your expense for every month are listed below,
    * January - 2200
    * February - 2350
    * March - 2600
    * April - 2130
    * May - 2190
'''
#Create a list to store these monthly expenses and using that find out
exp = [2200,2350,2600,2130,2190]
#1. In Feb, how many dollars you spent extra compare to January?
print("In feb this much extra was spent compared to jan:",exp[1]-exp[0])
#2. Find out your total expense in first quarter (first three months) of the year.
print("Expense for first quarter:",exp[0]+exp[1]+exp[2])
#3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month? ", 2000 in exp)
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print("Expenses at the end of June:",exp)
#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp)


'''Leetcode - Two sums
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
https://leetcode.com/problems/two-sum/solution/
'''

#O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            goal = target - nums[i]
            if (goal in nums[i+1:]):
                index2 = nums[i+1:].index(goal) + i + 1
                return [i,index2]
#Fastest 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i