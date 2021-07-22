'''
Arrays

Definition
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

'''  Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #setup
        merged_array = nums1 + nums2
        array = merged_array.sort()
        arr_length = len(merged_array)
        middle_arr = math.ceil(arr_length/2)
        #odd length just grab the middle
        if (len(merged_array) %2 == 1):
            return merged_array[middle_arr-1]
        #Even length do more work
        else:
            median = (merged_array[middle_arr-1] + merged_array[middle_arr])/2
            return median
        

'''Leetcode - Three sums
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

https://leetcode.com/problems/3sum/

'''
def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Edge cases
        if nums is None or len(nums) < 2:
            return []
        arr = sorted(nums)
        result = set()
        for x in range(0,len(arr)-1):
            target = -arr[x]
            i = arr[x]
            j = x+1
            k = len(arr)-1
            while j < k:
                sum = arr[j] + arr[k]
                if sum < target:
                    j=j+1
                elif sum > target:
                    k=k-1
                else:
                    result.add((arr[x], arr[j], arr[k])) 
                    j=j+1
                    k=k-1
        return result