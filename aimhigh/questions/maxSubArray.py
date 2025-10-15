# Given an integer array nums, find the with the largest sum, and return its sum.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSub = nums[0] # Initiallize with the first element of the array

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
        return maxSub