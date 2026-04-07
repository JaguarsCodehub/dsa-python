# Consecutive ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]Output: 3Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]Output: 2

def findConsecutiveOnes(nums):
    if not nums:
        return 0
    
    count = 0
    maxCount = 0

    for num in nums:
        if num == 1:
            count += 1
            if count > maxCount:
                maxCount = count
        else:
            count = 0
        
    return maxCount

arr = [1,1,0,0,1,0,1,1,1,1,0]
print(findConsecutiveOnes(arr))