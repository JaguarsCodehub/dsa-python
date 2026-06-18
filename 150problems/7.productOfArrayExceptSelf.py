# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

def productsOfArrayExceptSelf(nums):

        print("Original Nums: ",nums)
        n = len(nums)
        leftProduct = 1
        rightProduct = 1

        answer = [1] * n
        print("Answer:", answer)

        for i in range(n):
            answer[i] *= leftProduct
            print("answer[i]:", answer[i])
            print("Before leftProduct:", leftProduct)
            leftProduct *= nums[i]
            print("After leftProduct:", leftProduct)

        
        for i in range(n - 1, -1, -1):
            answer[i] *= rightProduct
            print("answer[i]:", answer[i])
            print("Before rightProduct:", rightProduct)
            rightProduct *= nums[i]
            print("After rightProduct:", rightProduct)

        print("Final Answer:", answer)
        return answer
    
nums = [1,2,3,4]
print(productsOfArrayExceptSelf(nums))


# More Optimized version
def productsExceptSelf(nums):

    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res