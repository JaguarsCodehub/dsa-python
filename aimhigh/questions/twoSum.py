# 🔹 Problem Statement

# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# def twoSum(arr, target):
    
#     n = len(arr)

#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] + arr[j] == target:
#                 return [i, j]
            
def twoSum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    

arr = [2,7,11,15]
target = 9
print(twoSum(arr, target))